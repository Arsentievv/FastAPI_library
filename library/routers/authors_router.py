from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from library import schemas
from library import crud
from config import oauth2_scheme

router = APIRouter(tags=['author'])


@router.get("/get-authors-books/{author_id)", response_model=list[schemas.BookBase])
def get_authors_books(
        author_id: int,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    return crud.get_authors_books(db=db, author_id=author_id)


@router.get('/get-author/{author_id}', response_model=schemas.AuthorBase)
def get_author(
        author_id: int,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    return crud.get_author(db=db, author_id=author_id)


@router.get('/get-all-authors', response_model=list[schemas.AuthorBase])
def get_all_authors(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    return crud.get_all_authors(db=db)


@router.post('/create-author', response_model=schemas.AuthorBase)
def create_author(
        author: schemas.AuthorBase,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    return crud.create_author(db=db, author=author)
