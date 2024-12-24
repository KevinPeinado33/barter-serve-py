from flask import Blueprint, jsonify, request
from dependency_injector.wiring import Provide, inject

from src.domain.models.user_model import User
from src.applications.use_cases.user.register import RegisterUserUsecase
from src.applications.use_cases.user.sign_in import SignInUsecase
from src.adapters.injectors.container import Container

auth = Blueprint('auth', __name__)

@auth.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': 'Hello World!'})


@auth.route('/sign-in', methods=['POST'])
@inject
def sign_in(
    usecase: SignInUsecase = Provide[Container.singin_user_usecase]
):
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    try:
       
        user_found = usecase.execute(email, password)
        return jsonify({"message": "Sign in successful", "user": user_found.to_dict()}), 200
    
    except ValueError as e:
        if str(e) == 'User not found':
            return jsonify({"error": str(e)}), 404
        elif str(e) == 'Invalid password':
            return jsonify({"error": str(e)}), 401
        else:
            return jsonify({"error": "Bad request"}), 400

@auth.route('/register', methods=['POST'])
@inject
def register(
    usecase: RegisterUserUsecase = Provide[Container.register_user_usecase]
):
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    try:

        registered_user = usecase.execute( User(name, email, password) )
        return jsonify({"message": "User registered successfully", "user": registered_user.to_dict()}), 201
    
    except ValueError as e:
        if str(e) == 'User already exists':
            return jsonify({"error": str(e)}), 400
        else:
            return jsonify({"error": "Bad request"}), 400
