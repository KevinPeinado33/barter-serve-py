from dependency_injector import containers, providers

from src.adapters.datasources.mongodb.user_datasource import UserDataSourceMongodb
from src.applications.use_cases.user.register import RegisterUserUsecase
from src.applications.use_cases.user.sign_in import SignInUsecase

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(packages=["src.blueprints"])

    user_repository = providers.Factory(UserDataSourceMongodb)

    singin_user_usecase = providers.Factory(
        SignInUsecase,
        user_repository=user_repository
    )

    register_user_usecase = providers.Factory(
        RegisterUserUsecase,
        user_repository=user_repository
    )
