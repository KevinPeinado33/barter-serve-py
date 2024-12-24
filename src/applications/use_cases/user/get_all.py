from src.domain.repositories.user_repository import UserRepository

class GetAllUserUsecase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self):
        users = self.user_repository.get_all()

        if users:
            raise ValueError('Empty')
        
        return users
    