from flask import Blueprint, jsonify, request
from dependency_injector.wiring import Provide, inject
# from flask_restx import Namespace

from ..adapters.injectors import Container
from ..applications.use_cases import SignInUsecase

# users_ns = Namespace('Usuarios', description='Operaciones de usuarios')

auth = Blueprint('auth', __name__)

@auth.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': 'Hello World!'})

@auth.route('/sign-in', methods=['POST'])
@inject
def sign_user(
    usecase: SignInUsecase = Provide[Container.singin_user_usecase]
):
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    try:
        userFound = usecase.execute(email, password)
        return jsonify({"message": "Sign in successful", "user": userFound.to_dict()}), 200
    except ValueError as e:
        if str(e) == 'User not found':
            return jsonify({"error": str(e)}), 404
        elif str(e) == 'Invalid password':
            return jsonify({"error": str(e)}), 401
        else:
            return jsonify({"error": "Bad request"}), 400
