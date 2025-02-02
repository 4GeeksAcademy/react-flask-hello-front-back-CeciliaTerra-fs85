from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped
from typing import List
db = SQLAlchemy()



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)pi
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach        
        # }
    

    #mine

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=True)
    correo = mapped_column(String(100), nullable=False)
    contraseña = mapped_column(String(20), nullable=False)
    suscripcion = mapped_column(String(10), nullable=True)
    favoritosper: Mapped[List["Favoritos_personajes"]]= relationship()
    favoritospla: Mapped[List["Favoritos_planetas"]] = relationship()

    def serialize(self):#Cada modelo tiene método serialize() para convertir el objeto en un diccionario serializable (para JSON), no incluir contraseñas
        return {
            "id": self.id,
            "correo": self.correo
            # do not serialize the password, its a security breach
        }
    
class Planetas(db.Model):
    __tablename__ = "planetas"
    id = mapped_column(Integer, primary_key=True)
    nombre_planeta = mapped_column(String(50), nullable=False)
    poblacion = mapped_column(String(20), nullable=False)
    extension = mapped_column(String(10), nullable=False)
    favoritospla: Mapped[List["Favoritos_planetas"]] = relationship()

    def serialize(self):
        return {
            "id_planeta": self.id,
            "nombre_planeta": self.nombre_planeta
            # do not serialize the password, its a security breach
        }
    
class Personajes(db.Model):
    __tablename__ = "personajes"
    id = mapped_column(Integer, primary_key=True)
    nombre_personaje = mapped_column(String(50), nullable=False)
    color_de_ojos = mapped_column(String(100), nullable=False)
    color_de_pelo = mapped_column(String(20), nullable=False)
    altura_de = mapped_column(String(10), nullable=False)
    favoritosper: Mapped[List["Favoritos_personajes"]] = relationship()


    def serialize(self):
        return {
            "id": self.id,
            "nombre_personaje": self.nombre_personaje
            # do not serialize the password, its a security breach
        }

class Favoritos_personajes(db.Model):
    __tablename__ = "favoritos_personajes"
    id = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))   
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personajes.id"))

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,         
            "personaje_id": self.personaje_id
           
        }

    
class Favoritos_planetas(db.Model):
    __tablename__ = "favoritos_planetas"
    id = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planetas.id"))
    

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id       
           
        }
    
    