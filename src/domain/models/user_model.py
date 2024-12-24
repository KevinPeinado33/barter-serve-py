from uuid import uuid4
class User:
    def __init__(
            self, 
            name: str, 
            email: str,
            password: str,
            _id: str = None
        ):
        self._id = _id or str(uuid4())
        self.name = name
        self.password = password
        self.email = email

    
    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'email': self.email,
            'password': self.password
        }