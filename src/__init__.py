from flask import Flask
from .adapters.injectors import Container
import os
import sys
from flask_restx import Api

def create_app():

    app = Flask(__name__, instance_relative_config=True)
            
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    app.container = container

    api = Api(app, 
              version='1.0', 
              title='Mi API',
              description='Descripción de la API')

    # register blueprint 
    from .blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # api.add_namespace(users_ns)
   
    return app