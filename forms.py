from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class DemandasForm(FlaskForm):
    motivo = StringField('Motivo de la demanda', validators=[DataRequired(), Length(max=100)])
    nombre_completo = StringField('Nombre completo del individuo', validators=[DataRequired(), Length(max=100)])
    dni_individuo = StringField('DNI del individuo', validators=[DataRequired(), Length(max=50)])
    ano_nacimiento = IntegerField('Año de nacimiento', validators=[DataRequired()])
    numero_legajo = StringField('Número de legajo', validators=[DataRequired(), Length(max=100)])
    enviar = SubmitField('Registrar demanda')
