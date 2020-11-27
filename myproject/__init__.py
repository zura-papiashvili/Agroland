from flask import Flask, render_template,request,url_for,sessions,redirect
from flask_mail import Mail, Message
from myproject.forms import PlantsForms
#from myproject.test import choise_point,yes_no,precipitation,minfrost,mintemp
from collections import Counter

import pandas as pd
app = Flask(__name__)
mail= Mail(app)
app.config['SECRET_KEY'] = 'MrvlSecret'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mr.ktevzadze@gmail.com'
app.config['MAIL_PASSWORD'] = 'MrvlSecret'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/',methods=['GET', 'POST'] )
def index():
    names = ['plant','plant','plant','plant','plant','plant','plant','plant','plant','plant']
    scores = ['0','0','0','0','0','0','0','0','0','0']

    form=PlantsForms()
    if form.validate_on_submit():

        df = pd.read_csv('data.csv', encoding='utf8')

        samp = df.iloc[2][1:]
        samp['Adapted to Coarse Textured Soils'] = form.Coarse.data
        samp['Adapted to Medium Textured Soils'] = form.Medium.data
        samp['Adapted to Fine Textured Soils'] = form.Fine.data
        samp['CaCO<SUB>3</SUB> Tolerance'] = form.CaCO.data
        samp['Cold Stratification Required'] = form.Cold.data
        samp['Frost Free Days, Minimum'] = form.Frost_free.data
        samp['Moisture Use'] = form.Moisture.data
        samp['pH (Minimum)'] = form.pH_Min.data
        samp['pH (Maximum)'] = form.pH_Max.data
        samp['Precipitation (Minimum)'] = form.Precipitation_min.data
        samp['Precipitation (Maximum)'] = form.Precipitation_max.data
        samp['Temperature, Minimum (°F)'] = form.temperature_min.data


        def choise_point(col, plant, samp):
            choise = {'Any': 'Any', 'None': 0, 'Low': 1,
                      'Medium': 2, 'High': 3}
            try:

                point_samp = choise[samp[col]]
                point_df = choise[plant[col]]
                if plant[col] == samp[col] or samp[col] == 'Any':
                    return 1

                return 1 / (point_df - point_samp + 2) ** 2
            except:
                return 0.1

        def yes_no(col, plant, samp):
            if plant[col] == samp[col] or samp[col] == 'Any':
                return 1
            return 0

        def precipitation(plant, samp):
            col_min = samp['Precipitation (Minimum)']
            print(samp)
            col_max = samp['Precipitation (Maximum)']
            plant_min = plant['Precipitation (Minimum)']
            plant_max = plant['Precipitation (Maximum)']

            if col_min >= plant_min and col_max <= plant_max:
                return 1
            k = 0
            if col_min < plant_min:
                k += plant_min - col_min
            if col_max > plant_max:
                k += col_max - plant_max
            return 2 / (k + 3)

        def mintemp(plant, samp):
            col_t = samp['Temperature, Minimum (°F)'] * (9 / 5) + 32

            plant_t = plant['Temperature, Minimum (°F)']
            if col_t >= plant_t:
                return 1
            return 5 / (-col_t + plant_t + 10)

        def minfrost(col, plant, samp):
            col_f = samp[col]
            plant_f = plant[col]
            if col_f >= plant_f:
                return 1
            return 15 / (-col_f + plant_f + 40)

        def countpoint(plant, samp):
            s = 0
            plant = plant
            #########
            s += yes_no('Adapted to Coarse Textured Soils', plant, samp)

            #########
            s += yes_no('Adapted to Medium Textured Soils', plant, samp)

            ###########
            s += yes_no('Adapted to Fine Textured Soils', plant, samp)

            ###################################
            # s += choise_point('Anaerobic Tolerance', plant, samp)

            #################################
            s += choise_point('CaCO<SUB>3</SUB> Tolerance', plant, samp)

            ##################################
            s += yes_no('Cold Stratification Required', plant, samp)

            ##################################
            s += choise_point('Moisture Use', plant, samp)

            ##################################
            s += precipitation(plant, samp)

            ##############
            s += mintemp(plant, samp)

            ############
            s += minfrost('Frost Free Days, Minimum', plant, samp)

            #s += precipitation('pH (Minimum)', 'pH (Maximum)', plant, samp)

            return s

        plantsinfo = {}
        def calculate(df, samp):
            result = {}

            for plant in df.iloc:
                #result[plant[0]] = countpoint(plant, samp) / 11 * 100

                try:
                    result[plant[0]] = countpoint(plant, samp) / 11 * 100
                except:
                    result[plant[0]] = 0
            plantsinfo[plant[0]]=plant
            return dict(Counter(result).most_common(10))

        #plantsinfo={}
        #sessions['plantsinfo']='hi'

        result = calculate(df, samp)
        names = list(result.keys())
        scores = list(result.values())
        scores=[round(x) for x in scores ]


        return render_template('index.html',title="Company Name",form=form,names=names,scores=scores,plantsinfo=plantsinfo)
    k="49"
    plantsinfo={'plant':['Any','Any','Any','Any','Any','Any',0,0,0,0,0,0]}
    return render_template('index.html',title="Company Name",form=form,k=k,names=names,scores=scores)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    data = request.args
    user_name = data.get("first_name")
    user_last_name = data.get("last_name")
    user_mail = data.get("email")
    user_text = data.get("text")

    if user_text!=None:

        msg = Message(user_name, sender='mr.ktevzadze@gmail.com', recipients=['mr.ktvezadze@gmail.com',user_mail])
        msg.body = f"Dear {user_name},\n your mail({user_text})was successfully sent to the company mail.\n\nBest Regards,\nCarlo "
        msg.title = 'title'
        mail.send(msg)
    return render_template('contact.html',title='contact')

@app.route('/info',methods=['GET','POST'])
def info():

    return render_template('info.html')




