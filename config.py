from pydantic_settings import BaseSettings
from fastapi.security import OAuth2PasswordBearer
from pydantic import Field
from typing import Union
from pathlib import Path


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class LibraryBaseSettings(BaseSettings):
    PROJECT_NAME: str = 'FastAPI Library'
    API_VERSION_INT: int = 1
    BASE_API_PREFIX: str = f'/api/v{API_VERSION_INT}'
    BASE_DIR: str = str(Path().absolute())

    class ConfigDict:
        extra = 'allow'
        env_file = '.env'
        case_sensitive = True


class PGSettings(LibraryBaseSettings):
    POSTGRES_DB: str = Field('library', title='PG DB name')
    POSTGRES_USER: str = Field('postgres', title='PG DB user')
    POSTGRES_PASSWORD: str = Field('postgres', title='PG DB password')
    POSTGRES_HOST: str = Field('localhost', title='PG DB host')
    POSTGRES_PORT: str = Field('5432', title='PG DB port')
    # POSTGRES_DRIVER: str = 'postgresql+asyncpg'
    POSTGRES_DRIVER: str = 'postgresql'

    @property
    def sqlalchemy_db_uri(self) -> str:
        return f"{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" \
               f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


class LibrarySettings(LibraryBaseSettings):
    SECRET_KEY: str = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool = Field(True)
    postgres: PGSettings = PGSettings()


def get_settings(db_only=False) -> Union[PGSettings, LibrarySettings]:
    return PGSettings() if db_only else LibrarySettings()

