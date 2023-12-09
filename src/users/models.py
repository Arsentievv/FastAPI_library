from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    full_name = Column(String, nullable=True)
    disabled = Column(Boolean, default=False)

    def __repr__(self):
        return f'id:{self.id} username: {self.username}'
