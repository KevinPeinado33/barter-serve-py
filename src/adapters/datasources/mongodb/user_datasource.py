from src.domain.models import User
from src.domain.repositories import UserRepository

class UserDataSourceMongodb(UserRepository):
    
    def __init__(self):
        self.users = {
            1: User("John Doe", "jhondoe@gmail.com", "123456"),
            2: User("Jane Doe", "janedoe@gmail.com", "654321")
        }

    def get_by_email(self, email: str) -> User:
        for user in self.users.values():
            if user.email == email:
                return user
        return None
    
    def create(self, user: User) -> User:
        self.users[user.email] = user
        return user
    
    def get(self, id: int) -> User:
        return self.users.get(id)
    
    def update(self, user: User) -> User:
        self.users[user.email] = user
        return user
    
    def delete(self, id: int) -> None:
        del self.users[id]
