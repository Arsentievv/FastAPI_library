from pydantic import BaseModel, HttpUrl
from datetime import datetime


class BookBase(BaseModel):
    title: str
    description: str
    date_of_publish: datetime


class ShopBase(BaseModel):
    title: str
    url: str
    address: str | None = None


class ShopCreate(ShopBase):
    pass

    class Config:
        orm_mode = True


class Shop(ShopBase):
    id: int
    books: list[BookBase]

    class Config:
        orm_mode = True

class Book(BookBase):
    id: int
    shops: list[Shop]

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



