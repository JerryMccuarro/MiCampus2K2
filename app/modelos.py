from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class TablaCalificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String,nullable=False, index=True)
    apellido = db.Column(db.String, nullable=False,index=True)
    matricula = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String,nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean,nullable=False, default=True)

class TablaUsuario(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String,nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    esAdmin = db.Column(db.Boolean,nullable=False, default=False)
    isActive = db.Column(db.Boolean,nullable=False, default=True)

    def set_password(self,password):
        if len(password)>5:
            self.password_hash = generate_password_hash(password)
            return True
        return False

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def user_loader(id):
    return TablaUsuario.query.get(id)