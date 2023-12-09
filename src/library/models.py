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


class BookShop(Base):
    __tablename__ = 'books_shops'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    date_of_publish = Column(DATE, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    owner = relationship("Author", back_populates="books")
    shops = relationship("Shop", secondary="books_shops", back_populates="books")

    def __repr__(self):
        return f'id: {self.id} title: {self.title}'


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=200), nullable=False, index=True)
    address = Column(String(length=200), nullable=True)
    url = Column(String(length=200), nullable=False)

    books = relationship("Book", secondary="books_shops", back_populates="shops")

    def __repr__(self):
        return f'id: {self.id} title: {self.title}'
