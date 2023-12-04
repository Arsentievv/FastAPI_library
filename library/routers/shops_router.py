from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from library import schemas
from config import oauth2_scheme
from typing import Annotated, List
from database import get_db
from library import crud

router = APIRouter(tags=['shops'])


@router.get('/shops/all', response_model=List[schemas.Shop])
def get_all_shops(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)],
        shops: Annotated[List[schemas.Shop], crud.get_all_shops]
):
    return shops


@router.post('/shops/create', response_model=schemas.Shop)
def create_shop(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)],
        shop: schemas.ShopCreate
):
    return crud.create_shop(db=db, shop=shop)


@router.get('/shops/books/{book_id}', response_model=schemas.ShopBase)
def shops_with_book(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)],
        book_id: int
):
    shops = crud.get_shops_with_book(db=db, book_id=book_id)
    return shops


@router.post('/shops/add-book-to-shop/{book_id}/{shop_id}')
def add_book_to_shop(
        db: Annotated[Session, Depends(get_db)],
        book_id: int,
        shop_id: int
):
    result = crud.add_book_in_shop(db=db, book_id=book_id, shop_id=shop_id)
    return result

