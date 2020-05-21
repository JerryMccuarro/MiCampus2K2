from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email, NumberRange, EqualTo

class FormaAlta(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(message="Este campo en obligatorio.")])
    apellido = StringField("Apellido", validators=[DataRequired(message="Este campo en obligatorio.")])
    matricula = IntegerField("Matricula",validators=[DataRequired(message="Este campo en obligatorio.")])
    materia = SelectField("Materia",validators=[DataRequired(message="Este campo en obligatorio.")],choices=[("POO","Programacion orientada a objetos"),
                                                                         ("esp","Español"),
                                                                         ("mate","Matematicas")])
    calificacion = IntegerField("Calificacion",validators=[DataRequired(message="Este campo en obligatorio."),NumberRange(min=0,max=100,message="Solo entre 0 y 100")])
    guardar = SubmitField("Guardar")


class FormaLogin(FlaskForm):
    email = StringField("Email",validators=[DataRequired(message="Ingresa un correo"),Email(message="Ingresa un correo valido")])
    password = PasswordField("Password",validators=[DataRequired(message="Ingresa una clave")])
    submit = SubmitField("Login")


class FormaCreaUsuario(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Ingresa un correo"),
                                             Email(message="Ingresa un correo valido")])
    password = PasswordField("Password", validators=[DataRequired(message="Ingresa una clave"), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField("Password", validators=[DataRequired(message="Ingresa una clave")])
    submit = SubmitField("Crear Usuario")