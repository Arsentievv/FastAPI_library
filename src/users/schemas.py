from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    disabled: bool = False


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None