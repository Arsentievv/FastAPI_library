from fastapi import FastAPI
from users.router import router as users_router
from library.routers import books_router, authors_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Library', debug=True)

app.include_router(users_router)
app.include_router(books_router.router)
app.include_router(authors_router.router)







