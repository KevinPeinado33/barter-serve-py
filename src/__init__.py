from flask import Flask
from flask_restx import Api
import sys
from .adapters.injectors.container import Container
from .adapters.config.mongo_client import get_db

def create_app():

    app = Flask(__name__, instance_relative_config=True)
            
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    app.container = container
    app.mongodb = get_db()


    api = Api(app, 
              version='1.0', 
              title='Mi API',
              description='Descripción de la API')

    # register blueprint 
    from .blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # api.add_namespace(users_ns)
   
    return app