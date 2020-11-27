



from collections import Counter
from myproject.forms import PlantsForms
form=PlantsForms()


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

    # s += precipitation('pH (Minimum)', 'pH (Maximum)', plant, samp)

    return s

def creatSamp(form,df):
    samp = df.iloc[2][1:]
    samp['Adapted to Coarse Textured Soils'] = form.Coarse.data
    samp['Adapted to Medium Textured Soils'] = form.Medium.data
    samp['Adapted to Fine Textured Soils'] = form.Fine.data
    #samp['Anaerobic Tolerance'] = form.Anaerobic.data
    samp['CaCO<SUB>3</SUB> Tolerance'] = form.CaCO.data
    samp['Cold Stratification Required'] = form.Cold.data
    #samp['Drought Tolerance'] = form.Drought.data
    #samp['Fertility Requirement'] = form.Fertility.data
    #samp['Fire Tolerance'] = form.Fire.data
    samp['Frost Free Days, Minimum'] = form.Frost_free.data
    samp['Moisture Use'] = form.Moisture.data
    #samp['Hedge Tolerance'] = form.Hedge.data
    samp['pH (Minimum)'] = form.pH_Min.data
    samp['pH (Maximum)'] = form.pH_Max.data
    #samp['Planting Density per Acre, Minimum'] = form.plant_density_min.data
    #samp['Planting Density per Acre, Maximum '] = form.plant_density_max.data
    samp['Precipitation (Minimum)'] = form.Precipitation_min.data
    samp['Precipitation (Maximum)'] = form.Precipitation_max.data
    #samp['Root Depth, Minimum (inches)'] = form.root_depth_min.data
    #samp['Salinity Tolerance'] = form.Salinity.data
    #samp['Shade Tolerance'] = form.Shade.data
    samp['Temperature, Minimum (°F)'] = form.temperature_min.data
    return samp