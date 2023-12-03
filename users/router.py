from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config import get_settings
from database import get_db
from users import crud as users_crud
from users import utils as users_utils
from users import schemas as users_schemas

router = APIRouter(
    tags=['users']
)

settings = get_settings()


@router.post('/create-user', response_model=users_schemas.UserBase)
def create_user(user: users_schemas.UserCreate, db: Session = Depends(get_db)):
    return users_crud.create_user(db=db, user=user)


@router.get('/users/me')
async def read_users_me(current_user: Annotated[users_schemas.User, Depends(users_crud.get_current_user)]):
    return current_user


@router.post('/token', response_model=users_schemas.Token)
def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
):
    user = users_utils.authenticate_user(
        db=db,
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password.',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = users_utils.create_access_token(
        data={'sub': user.username}, expire_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

