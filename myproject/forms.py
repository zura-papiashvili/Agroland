from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError,RadioField,IntegerField,SelectField
from wtforms.validators import DataRequired, Email, EqualTo,email_validator
from flask_wtf.file import FileField, FileAllowed



class PlantsForms(FlaskForm):
    Coarse = SelectField('Adapted to Coarse Textured Soils:',
                            choices=[('Any', 'Any'), ('Yes', 'Yes'),('No', 'No')])
    Medium = SelectField('Adapted to Medium Textured Soils:',
                        choices=[('Any', 'Any'), ('Yes', 'Yes'), ('No', 'No')])
    Fine = SelectField('Adapted to Fine Textured Soils:',
                        choices=[('Any', 'Any'), ('Yes', 'Yes'), ('No', 'No')])
    #Anaerobic = SelectField('Anaerobic Tolerance:',
                        # choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                        #           ('Medium', 'Medium'), ('High', 'High')])
    CaCO = SelectField('CaCO <sub>3</sub> Tolerance:',
                      choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                               ('Medium', 'Medium'), ('High', 'High')])
    Cold = SelectField('Cold Stratification Required:',
                        choices=[('Any', 'Any'), ('Yes', 'Yes'), ('No', 'No')])
    #Drought = SelectField('Drought Tolerance:',
                         # choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                         #          ('Medium', 'Medium'), ('High', 'High')])
    #Fertility = SelectField('Fertility Requirement:',
                           # choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                           #          ('Medium', 'Medium'), ('High', 'High')])
    #Fire = SelectField('Fire Tolerance:',
                        # choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                        #        ('Medium', 'Medium'), ('High', 'High')])
    Frost_free = IntegerField('Frost Free Days, Minimum:',validators=[DataRequired()])
    #Hedge = SelectField('Hedge Tolerance:',
                       # choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                       #          ('Medium', 'Medium'), ('High', 'High')])
    Moisture = SelectField('Moisture Use:',
                       choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
                                ('Medium', 'Medium'), ('High', 'High')])
    pH_Min = IntegerField('pH (Minimum):',validators=[DataRequired()])
    pH_Max = IntegerField('pH (Maximum):',validators=[DataRequired()])
    #plant_density_min = IntegerField('Planting Density per Acre, Minimum:', validators=[DataRequired()])
    #plant_density_max = IntegerField('Planting Density per Acre, Maximum:', validators=[DataRequired()])
    Precipitation_min = IntegerField('Precipitation (Minimum):', validators=[DataRequired()])
    Precipitation_max = IntegerField('Precipitation (Maximum):', validators=[DataRequired()])
    #root_depth_min = IntegerField('Root Depth, Minimum (inches):', validators=[DataRequired()])
    # #Salinity = SelectField('Salinity Tolerance:',
    #                       choices=[('Any', 'Any'), ('None', 'None'), ('Low', 'Low'),
    #                                ('Medium', 'Medium'), ('High', 'High')])
    # #Shade = SelectField('Shade Tolerance:',
    #                       choices=[('Any', 'Any'), ('Intolerant', 'Intolerant'), ('Intermediate', 'Intermediate'),
    #                                ('Tolerant', 'Tolerant')])
    temperature_min = IntegerField('Temperature, Minimum (°F):', validators=[DataRequired()])
    submit = SubmitField("Calculate")