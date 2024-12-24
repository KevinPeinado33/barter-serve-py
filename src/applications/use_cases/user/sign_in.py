from src.domain.repositories.user_repository import UserRepository

class SignInUsecase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)

        if user is None:
            raise ValueError('User not found')
        
        if user.password != password:
            raise ValueError('Invalid password')
        
        return user

    