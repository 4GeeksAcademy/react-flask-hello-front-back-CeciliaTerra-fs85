"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Usuarios, Planetas, Personajes, Favoritos_personajes, Favoritos_planetas
from api.utils import generate_sitemap, APIException
from sqlalchemy import select
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)



# @api.route('/usuarios', methods=['GET'])
# def handle_hello():

#      response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#      return jsonify(response_body), 200
 

# # # Create a route to authenticate your users and return JWTs. The
# # # create_access_token() function is used to actually generate the JWT.
# # @api.route("/login", methods=["POST"])
# # def login():
# #     try:
# #         email = request.json.get("email", None)
# #         password = request.json.get("password", None)
# #         user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()

# #         if email == user.email or password == user.password:
# #             access_token = create_access_token(identity=email)
# #             return jsonify(access_token=access_token), 200
            
# #     except:
# #          return jsonify({"msg": "Bad email or password"}), 401


# # # Protect a route with jwt_required, which will kick out requests
# # # without a valid JWT present.
# # @api.route("/profile", methods=["GET"])
# # @jwt_required()
# # def get_profile():
# #     # Access the identity of the current user with get_jwt_identity
# #     current_user = get_jwt_identity()
# #     print(current_user)
# #     return jsonify(logged_in_as=current_user), 200


# #mio

#GET de todos los usuarios ok
@api.route('/usuarios', methods=['GET'])
def handle_hello():
     data = db.session.scalars(select(Usuarios)).all()
     results = list(map(lambda item: item.serialize(),data))
     print(results)
     response_body = {
         "msg": "Hello, this are the usuarios ",
          "results": results
     } 
     return jsonify(response_body), 200

# #GET de todos los planetas ok
@api.route('/planetas', methods=['GET'])
def handle_planetas():
     data = db.session.scalars(select(Planetas)).all()
     results = list(map(lambda item: item.serialize(),data))
     print(results)
     response_body = {
          "msg": "Hello, this are the planets ",
          "results": results
     }
     return jsonify(response_body), 200

 #GET de todos los personajes ok
@api.route('/personajes', methods=['GET'])
def handle_personajes():
     data = db.session.scalars(select(Personajes)).all()
     results = list(map(lambda item: item.serialize(),data))
     print(results)
     response_body = {
         "msg": "Hello, this are the personajes ",
         "results": results
     }
     return jsonify(response_body), 200

# #GET de los favoritos personajes ok
@api.route('/favoritos-personajes', methods=['GET'])
def handle_favoritos_personajes():
     data = db.session.scalars(select(Favoritos_personajes)).all()
     results = list(map(lambda item: item.serialize(),data))
     print(results)
     response_body = {
         "msg": "Hello, this are the favoritos ",
         "results": results
     }
     return jsonify(response_body), 200


# #GET de los favoritos planetas
@api.route('/favoritos-planetas', methods=['GET'])
def handle_favoritos_planetas():
     data = db.session.scalars(select(Favoritos_planetas)).all()
     results = list(map(lambda item: item.serialize(),data))
     print(results)
     response_body = {
         "msg": "Hello, this are the favoritos ",
         "results": results
     }
     return jsonify(response_body), 200


# #GET de un usuario unico ok
@api.route('/usuario/<int:id>', methods=['GET'])
def traer_usuario(id):
     usuario = db.session.execute(select(Usuarios).filter_by(id=id)).scalar_one()

     response_body = {
         "msg": "Hello, this is your GET /user response ",
         "result":usuario.serialize()
     }
     return jsonify(response_body), 200

# #GET de un planeta unico ok
@api.route('/planeta/<int:id>', methods=['GET'])
def traer_planeta(id):
     planeta = db.session.execute(select(Planetas).filter_by(id=id)).scalar_one()

     response_body = {
         "msg": "Hello, this is your planeta ",
         "result":planeta.serialize()
     }
     return jsonify(response_body), 200

# #GET de un personaje unico
@api.route('/personaje/<int:id>', methods=['GET'])
def traer_personaje(id):
     personaje = db.session.execute(select(Personajes).filter_by(id=id)).scalar_one()

     response_body = {
         "msg": "Hello, this is your personaje ",
         "result":personaje.serialize()
     }
     return jsonify(response_body), 200


# #GET de un favorito unico
# @api.route('/favorito-personaje/<int:id>', methods=['GET'])
# def traer_personaje_favorito(id):
#     favorito = db.session.execute(select(Favoritos_personajes).filter_by(id=id)).scalar_one()

#     response_body = {
#         "msg": "Hello, this is your favorito ",
#         "result":favorito.serialize()
#     }
#     return jsonify(response_body), 200



# #Metodo POST para crear un usuario, envio los datos a la base de datos
# @api.route('/usuario', methods=['POST'])
# def crear_usuario():
#     request_data = request.json
#     usuario = Usuarios(correo=request_data["correo"], contraseña=request_data["contraseña"])
#     db.session.add(usuario)
#     db.session.commit()

#     response_body = {
#         "msg": "Hello, this is your usuario ",
#         "result":request_data
#     }
#     return jsonify(response_body), 200

# #Metodo POST para crear un planeta, envio los datos a la base de datos
# @api.route('/planeta', methods=['POST'])
# def crear_planeta():
#     request_data = request.json
#     planeta= Planetas(nombre_planeta=request_data["nombre_planeta"], poblacion=request_data["poblacion"], extension=request_data["extension"])
#     db.session.add(planeta)
#     db.session.commit()

#     response_body = {
#         "msg": "Hello, this is your new planeta ",
#         "result":request_data
#     }
#     return jsonify(response_body), 200

# #Metodo POST para crear un personaje, envio los datos a la base de datos
# @api.route('/personaje', methods=['POST'])
# def crear_personaje():
#     request_data = request.json
#     personaje= Personajes(nombre_personaje=request_data["nombre_personaje"], color_de_ojos=request_data["color_de_ojos"], color_de_pelo=request_data["color_de_pelo"])
#     db.session.add(personaje)
#     db.session.commit()

#     response_body = {
#         "msg": "Hello, this is your new personaje ",
#         "result":request_data
#     }
#     return jsonify(response_body), 200



# #POST favoritos, agregar planeta a favorito
# @api.route('/favoritos-planeta', methods=['POST'])
# def crear_planeta_favorito():
#     request_data = request.json
#     planeta_favorito= Favoritos_planetas(planeta_id=request_data["planeta_id"], usuario_id=request_data["usuario_id"])
#     db.session.add(planeta_favorito)
#     db.session.commit()

#     response_body = {
#         "msg": "Hello, this is your planeta favorito ",
#         "result":request_data
#     }
#     return jsonify(response_body), 200


# #POST favoritos, agregar personaje a favorito
# @api.route('/favoritos-personaje', methods=['POST'])
# def crear_personaje_favorito():
#     request_data = request.json
#     personaje_favorito= Favoritos_personajes(personaje_id=request_data["personaje_id"], usuario_id=request_data["usuario_id"])
#     db.session.add(personaje_favorito)
#     db.session.commit()

#     response_body = {
#         "msg": "Hello, this is your personaje favorito ",
#         "result":request_data
#     }
#     return jsonify(response_body), 200



# #Metodo DELETE de un usuario
# @api.route('/usuario/<int:id>', methods=['DELETE'])
# def borrar_usuario(id):
         
#         usuario = db.session.execute(select(Usuarios).filter_by(id=id)).scalar_one_or_none() #si no eso este metodo , no puedo gestionar el not found  
#         if usuario is None:
#             return jsonify({"msg": "Usuario not found"}), 400#error por parte de peticion
#         db.session.delete(usuario)
#         db.session.commit()
   
#         response_body = {
#         "msg": "Usuario eliminado"       
#     }
        
#         return jsonify(response_body), 200  
# #Metodo delete, uso select para buscar en la tabla la id del usuarios por el id dado, el metodo .scalar_one() me da un unico resultado, o me devuelve excepcion, el db.session.delete(usuario)
# #marca el usuario para ser eliminado en la base de datos (db, base de datos),db.session.commit() ejecuta los cambios en la base de datos, si no hago esto no funcionara 
# #el delete

# #Metodo DELETE de un personaje
# @api.route('/personaje/<int:id>', methods=['DELETE'])
# def borrar_personaje(id):
         
#         personaje = db.session.execute(select(Personajes).filter_by(id=id)).scalar_one_or_none() #si no eso este metodo , no puedo gestionar el not found  
#         if personaje is None:
#             return jsonify({"msg": "Personaje not found"}), 400#error por parte de peticion
#         db.session.delete(personaje)
#         db.session.commit()
   
#         response_body = {
#         "msg": "Personaje eliminado"       
#     }
        
#         return jsonify(response_body), 200  

# #Metodo DELETE de un planeta
# @api.route('/planeta/<int:id>', methods=['DELETE'])
# def borrar_planeta(id):
         
#         planeta = db.session.execute(select(Planetas).filter_by(id=id)).scalar_one_or_none() #si no eso este metodo , no puedo gestionar el not found  
#         if planeta is None:
#             return jsonify({"msg": "Planeta not found"}), 400#error por parte de peticion
#         db.session.delete(planeta)
#         db.session.commit()
   
#         response_body = {
#         "msg": "Planeta eliminado"       
#     }
        
#         return jsonify(response_body), 200  

# #Metodo DELETE de un planeta favorito
# @api.route('/favoritos-planeta/<int:id>', methods=['DELETE'])
# def borrar_planeta_favorito(id):
         
#         favorito = db.session.execute(select(Favoritos_planetas).filter_by(id=id)).scalar_one_or_none() #si no eso este metodo , no puedo gestionar el not found  
#         if favorito is None:
#             return jsonify({"msg": "Favorito not found"}), 400#error por parte de peticion
#         db.session.delete(favorito)
#         db.session.commit()
   
#         response_body = {
#         "msg": "Favorito eliminado"       
#     }
        
#         return jsonify(response_body), 200  



# #Metodo DELETE de un personaje favorito
# @api.route('/favoritos-personaje/<int:id>', methods=['DELETE'])
# def borrar_personaje_favorito(id):
         
#         favorito = db.session.execute(select(Favoritos_personajes).filter_by(id=id)).scalar_one_or_none() #si no eso este metodo , no puedo gestionar el not found  
#         if favorito is None:
#             return jsonify({"msg": "Favorito not found"}), 400#error por parte de peticion
#         db.session.delete(favorito)
#         db.session.commit()
   
#         response_body = {
#         "msg": "Favorito eliminado"       
#     }
        
#         return jsonify(response_body), 200  

@api.route("/login", methods=["POST"])
def login():
     print(request.json)
     correo = request.json.get("correo", None)
     contraseña = request.json.get("contraseña", None)
     usuario = Usuarios.query.filter_by(correo = correo, contraseña = contraseña).first()#me devolvera un elemento que cumpla las condiciones
     if not usuario:
          return jsonify({"msg": "Bad username or password"}), 401
     
     access_token = create_access_token(identity=correo)
     return jsonify(access_token=access_token)




@api.route("/profile", methods=["GET"])
@jwt_required()
def protected():
     #  Access the identity of the current user with get_jwt_identity
      current_user = get_jwt_identity()
      return jsonify(logged_in_as=current_user), 200
  

