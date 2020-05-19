from app import db

class TablaCalificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String,nullable=False, index=True)
    apellido = db.Column(db.String, nullable=False,index=True)
    matricula = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String,nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean,nullable=False, default=True)