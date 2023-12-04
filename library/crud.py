from passlib.context import CryptContext
from sqlalchemy.orm import Session, joinedload
from library import models
from library import schemas
from fastapi import HTTPException, status


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_all_authors(db: Session):
    return db.query(models.Author).all()


def create_author(db: Session, author: schemas.AuthorBase):
    db_author = models.Author(
        first_name=author.first_name,
        last_name=author.last_name,
        date_of_birth=author.date_of_birth
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_all_books(db: Session):
    return db.query(models.Book).all()


def get_authors_books(db: Session, author_id: int):
    return db.query(models.Book).filter(models.Book.author_id == author_id)


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        description=book.description,
        date_of_publish=book.date_of_publish,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def create_shop(db: Session, shop: schemas.ShopCreate):
    db_shop = models.Shop(
        title=shop.title,
        address=shop.address,
        url=shop.url
    )
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)

    return db_shop


def get_all_shops(db: Session):
    return db.query(models.Shop).all()


def get_shop(db: Session, shop_id: int):
    return db.query(models.Shop).filter(models.Shop.id == shop_id).first()


def get_shops_with_book(db: Session, book_id: int):
    pass


def add_book_in_shop(db: Session, book_id: int, shop_id: int):
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='Invalid input data',
    )
    shop = db.query(models.Shop).get(shop_id)
    if not shop:
        raise exception
    book = db.query(models.Book).get(book_id)
    if not book:
        raise exception
    shop.books.append(book)
    db.commit()
    db.refresh(shop)
    return shop
