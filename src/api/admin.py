import os
from flask_admin import Admin
from api.models import db, Usuarios, Planetas, Personajes, Favoritos_personajes, Favoritos_planetas
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class UserForm(FlaskForm):
        correo = StringField('Correo', [validators.DataRequired()])
        contraseña = PasswordField('Contraseña', [validators.DataRequired()])
        is_active = BooleanField('Is Active')

    class UserAdmin(ModelView):
        form = UserForm
        colum_list = ('correo', 'contraseña', 'is_active')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(UserAdmin(Usuarios, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Personajes, db.session))
    admin.add_view(ModelView(Favoritos_personajes, db.session))
    admin.add_view(ModelView(Favoritos_planetas, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))