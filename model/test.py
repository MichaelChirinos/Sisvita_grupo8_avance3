from utils.db import db
from datetime import date
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    __tablename__='test'
    id_test = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    total_Inquietud= db.Column(db.Integer)
    Categoria_Inquietud = db.Column(db.String(100))
    total_Ansiedad_Fisiologica= db.Column(db.Integer)
    Categoria_Ansiedad_Fisiologica = db.Column(db.String(100))
    total_Estres_Preocupaciones= db.Column(db.Integer)
    Categoria_Estres_Preocupaciones = db.Column(db.String(100))
    total_Ansiedad_Examenes= db.Column(db.Integer)
    Categoria_Ansiedad_Examenes = db.Column(db.String(100))
    total_Mentira= db.Column(db.Integer)
    Categoria_Mentira = db.Column(db.String(100))


    estudiante = db.relationship('Estudiante', backref='tests')
    
    def __init__(self, id_test, id_estudiante, total_Inquietud,Categoria_Inquietud, total_Ansiedad_Fisiologica,Categoria_Ansiedad_Fisiologica, total_Estres_Preocupaciones,Categoria_Estres_Preocupaciones, total_Ansiedad_Examenes,Categoria_Ansiedad_Examenes, total_Mentira,Categoria_Mentira):
        self.id_test = id_test
        self.id_estudiante = id_estudiante
        self.total_Inquietud = total_Inquietud
        self.Categoria_Inquietud = Categoria_Inquietud
        self.total_Ansiedad_Fisiologica = total_Ansiedad_Fisiologica
        self.Categoria_Ansiedad_Fisiologica = Categoria_Ansiedad_Fisiologica
        self.total_Estres_Preocupaciones = total_Estres_Preocupaciones
        self.Categoria_Estres_Preocupaciones = Categoria_Estres_Preocupaciones
        self.total_Ansiedad_Examenes = total_Ansiedad_Examenes
        self.Categoria_Ansiedad_Examenes = Categoria_Ansiedad_Examenes
        self.total_Mentira = total_Mentira
        self.Categoria_Mentira = Categoria_Mentira
