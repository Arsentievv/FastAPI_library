from typing import Annotated

from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from database import get_db
from config import get_settings
from config import oauth2_scheme
from users import models
from users import schemas
from users.schemas import TokenData
from users.utils import get_password_hash


settings = get_settings()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        password=get_password_hash(user.password),
        email=user.email,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user:
        return user


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user
