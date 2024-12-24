from bson.objectid import ObjectId

from src.domain.models.user_model import User
from src.domain.repositories.user_repository import UserRepository
from src.adapters.config.mongo_client import get_db

class UserDataSourceMongodb(UserRepository):
    
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['users']

    def create(self, user: User) -> User:
        user_dict = user.__dict__
        result = self.collection.insert_one(user_dict)
        user._id = str(result.inserted_id)
        return user
    
    def get(self, id: int) -> User:
        user_data = self.collection.find_one({'_id': ObjectId(id)})
        if user_data:
            return User(**user_data)
        return None
    
    def update(self, user: User) -> User:
        user_dict = user.__dict__
        user_id = user_dict.pop('_id')
        self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': user_dict})
        return user
    
    def delete(self, id: int) -> None:
        self.collection.delete_one({'_id': ObjectId(id)})

    def get_all(self) -> list[User]:
        return [User(**user) for user in self.collection.find()]
    
    def get_by_email(self, email: str) -> User:
        user_data = self.collection.find_one({'email': email})
        if user_data:
            return User(**user_data)
        return None
