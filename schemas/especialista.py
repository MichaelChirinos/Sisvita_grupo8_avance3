from utils.ma import ma
from model.especialista import Especialista
from marshmallow import fields
from schemas.usuario import UsuarioSchema

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = (
            'id_especialista',
            'id_usuario',
            'codigo_especialista',
            'especialidad',
            'colegiado',
            'usuario'
        )

    usuario = fields.Nested(UsuarioSchema)

especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many=True)

