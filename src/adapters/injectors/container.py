from dependency_injector import containers, providers

from ..datasources.mongodb import UserDataSourceMongodb
from ...applications.use_cases import SignInUsecase

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(packages=["src.blueprints"])

    user_repository = providers.Factory(UserDataSourceMongodb)

    singin_user_usecase = providers.Factory(
        SignInUsecase,
        user_repository=user_repository
    )
