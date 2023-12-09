from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from library import schemas, crud
from typing import Annotated

from config import oauth2_scheme

router = APIRouter(tags=['books'])


@router.post("/books", response_model=schemas.Book)
def create_book(
        book: schemas.BookCreate,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)):
    book = crud.create_book(db=db, book=book)
    return book


@router.get("/all-books", response_model=list[schemas.BookBase])
def get_all_books(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    return crud.get_all_books(db=db)


@router.get("/get-book/{book_id}", response_model=schemas.BookBase)
def get_book(
        book_id: int,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    return crud.get_book(db=db, book_id=book_id)
