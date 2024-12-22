from abc import ABC, abstractmethod

from ..models import User

class UserRepository(ABC):
    
    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass
    
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
