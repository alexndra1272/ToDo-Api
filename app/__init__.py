from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config



db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    

    # Inicializar la base de datos
    db.init_app(app)

    # Inicializar el sistema de migraciones
    migrate = Migrate(app, db)

    # Importar los blueprints
    from .nota import nota as nota_blueprint

    # Registrar los blueprints
    app.register_blueprint(nota_blueprint)

    return app


# Inicializar la aplicación

app = create_app('development')

if __name__ == '__main__':

    app.run()