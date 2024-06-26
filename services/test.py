from flask import Blueprint, request, jsonify, make_response
from model.test import Test
from utils.db import db
from schemas.test import test_schema, tests_schema

test_routes = Blueprint('test', __name__)  # Crea un blueprint llamado 'test'

# Crear un nuevo test
@test_routes.route('/test/v1', methods=['POST'])
def crear_test():
    id_test = request.json.get("id_test")
    id_estudiante = request.json.get("id_estudiante")
    total_Inquietud= request.json.get("total_Inquietud")
    Categoria_Inquietud = request.json.get("Categoria_Inquietud")   
    total_Ansiedad_Fisiologica= request.json.get("total_Ansiedad_Fisiologica")
    Categoria_Ansiedad_Fisiologica = request.json.get("Categoria_Ansiedad_Fisiologica")  
    total_Estres_Preocupaciones= request.json.get("total_Estres_Preocupaciones")
    Categoria_Estres_Preocupaciones = request.json.get("Categoria_Estres_Preocupaciones")  
    total_Ansiedad_Examenes= request.json.get("total_Ansiedad_Examenes")
    Categoria_Ansiedad_Examenes = request.json.get("Categoria_Ansiedad_Examenes")  
    total_Mentira= request.json.get("total_Mentira")
    Categoria_Mentira = request.json.get("Categoria_Mentira")  
    
    nuevo_test = Test(id_test, id_estudiante, total_Inquietud, Categoria_Inquietud, total_Ansiedad_Fisiologica,Categoria_Ansiedad_Fisiologica ,total_Estres_Preocupaciones, Categoria_Estres_Preocupaciones, total_Ansiedad_Examenes, Categoria_Ansiedad_Examenes, total_Mentira,Categoria_Mentira )
    db.session.add(nuevo_test)
    db.session.commit()

    result = test_schema.dump(nuevo_test)

    data = {
        'message': 'Test creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)


# Listar todos los tests
@test_routes.route('/test/v1/listar', methods=['GET'])
def listar_tests():
    all_tests = Test.query.all()
    result = tests_schema.dump(all_tests)

    data = {
        'message': 'Tests recuperados correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


# Obtener un test por su ID
@test_routes.route('/test/v1/<int:id>', methods=['GET'])
def obtener_test(id):
    test = Test.query.get(id)

    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = test_schema.dump(test)

    data = {
        'message': 'Test recuperado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Actualizar un test por su ID
@test_routes.route('/test/v1/<int:id>', methods=['PUT'])
def actualizar_test(id):
    nuevo_test = Test.query.get(id)

    if not nuevo_test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    id_test = request.json.get("id_test")
    id_estudiante = request.json.get("id_estudiante")
    total_Inquietud= request.json.get("total_Inquietud")
    Categoria_Inquietud = request.json.get("Categoria_Inquietud")   
    total_Ansiedad_Fisiologica= request.json.get("total_Ansiedad_Fisiologica")
    Categoria_Ansiedad_Fisiologica = request.json.get("Categoria_Ansiedad_Fisiologica")  
    total_Estres_Preocupaciones= request.json.get("total_Estres_Preocupaciones")
    Categoria_Estres_Preocupaciones = request.json.get("Categoria_Estres_Preocupaciones")  
    total_Ansiedad_Examenes= request.json.get("total_Ansiedad_Examenes")
    Categoria_Ansiedad_Examenes = request.json.get("Categoria_Ansiedad_Examenes")  
    total_Mentira= request.json.get("total_Mentira")
    Categoria_Mentira = request.json.get("Categoria_Mentira") 
    
    nuevo_test.id_test = id_test
    nuevo_test.id_estudiante = id_estudiante
    nuevo_test.total_Inquietud = total_Inquietud
    nuevo_test.Categoria_Inquietud = Categoria_Inquietud
    nuevo_test.total_Ansiedad_Fisiologica = total_Ansiedad_Fisiologica
    nuevo_test.Categoria_Ansiedad_Fisiologica = Categoria_Ansiedad_Fisiologica
    nuevo_test.total_Estres_Preocupaciones = total_Estres_Preocupaciones
    nuevo_test.Categoria_Estres_Preocupaciones = Categoria_Estres_Preocupaciones
    nuevo_test.total_Ansiedad_Examenes = total_Ansiedad_Examenes
    nuevo_test.Categoria_Ansiedad_Examenes = Categoria_Ansiedad_Examenes
    nuevo_test.total_Mentira = total_Mentira
    nuevo_test.Categoria_Mentira = Categoria_Mentira


    db.session.commit()

    result = test_schema.dump(nuevo_test)

    data = {
        'message': 'Test actualizado correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)


# Eliminar un test por su ID
@test_routes.route('/test/v1/<int:id>', methods=['DELETE'])
def eliminar_test(id):

    predio = Test.query.get(id)

    if not predio:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(predio)
    db.session.commit()

    data = {
        'message': 'Test eliminado correctamente',
        'status': 202
    }

    return make_response(jsonify(data), 202)