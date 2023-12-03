from sqlalchemy import Column, ForeignKey, Integer, String, DATE
from sqlalchemy.orm import relationship
from database import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    date_of_birth = Column(DATE, nullable=True)

    books = relationship("Book", back_populates="owner")

    def __repr__(self):
        return f'id: {self.id} last name: {self.last_name}'


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    date_of_publish = Column(DATE, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    owner = relationship("Author", back_populates="books")

    def __repr__(self):
        return f'id: {self.id} title: {self.title}'
