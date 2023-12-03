from pydantic import BaseModel
from datetime import datetime


class BookBase(BaseModel):
    title: str
    description: str
    date_of_publish: datetime


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    author_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: datetime


class Author(AuthorBase):
    id: int
    books: list[Book] = []

    class Config:
        orm_mode = True

