from abc import ABC, abstractmethod

from ..models.user_model import User

class UserRepository(ABC):
    
    @abstractmethod
    def get(self, id: int) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass
    