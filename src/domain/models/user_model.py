from uuid import uuid4
class User:
    def __init__(
            self, 
            name: str, 
            email: str,
            password: str,
            id: None = uuid4()
        ):
        self.id = id
        self.name = name
        self.password = password
        self.email = email

    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password
        }