from src.domain.repositories.user_repository import UserRepository
from src.domain.models.user_model import User

class RegisterUserUsecase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user: User):
        user_registered = self.user_repository.get_by_email(user.email)

        if user_registered:
            raise ValueError('User already exists')
        
        return self.user_repository.create(user)
    