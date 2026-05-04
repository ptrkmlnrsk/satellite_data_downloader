from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.authorization.auth import authenticate_google_api, initialize_earth_engine
from src.api.pipelines import router as pipeline_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    credentials = authenticate_google_api()
    initialize_earth_engine(credentials)

    print("Earth Engine initialized successfully!")

    yield

    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(pipeline_router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}


# from dataclasses import dataclass
#
# from fastapi import FastAPI, Depends
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session, sessionmaker
# from pydantic import BaseModel, ConfigDict
#
#
# DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()
#
# app = FastAPI()
#
#
# class UserDB(Base):
#    __tablename__ = "users"
#    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
#    name: Mapped[str]
#    age: Mapped[int]
#
#
# Base.metadata.create_all(engine) # laduje wszystkie modele ktore sa w calym projekcie
## nie robic tego gdy jest to w produkcji
#
#
# class UserCreate(BaseModel): # walidacja czy uzytkownik ma podać ID? no raczej nie
#    name: str
#    age: int
#
#
# class UserRead(BaseModel): #odczyt usera
#    id: int
#    name: str
#    age: int
#
#    model_config = ConfigDict(from_attributes=True) # konwertuje to co robimy w bazie na pydantica
#
#
# def get_db():
#    session=SessionLocal()
#    try:
#        yield session
#    finally:
#        session.close()
#
#
# @app.post("/users/", response_model=UserRead) # response_model=UserRead to zwraca pydantic model
# def create_user(user: UserCreate, db: Session = Depends(get_db)): # jesli cos tu bedzie zle z UserCreate to bedzie krzyczec
#    db_user = UserDB(name=user.name, age=user.age) # stworzony model ORM, nie ma tu walidacji
#    db.add(db_user)
#    db.commit()
#    db.refresh(db_user) # ściągniecie najnowszego stanu obiektu w bazie
#    return db_user
#
#
################
#
# class User:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        self.height = 1.75
#
#    def __repr__(self):
#        return f"User(name={self.name}, age={self.age}, height={self.height})"
#
#    def __str__(self):
#        return f"{self.name} is {self.age} years old."
#
#
#
# u = User("John", 36)
# print(u)
#
# @dataclass
# class User2:
#    name : str
#    age : int
#    height : float = 1.75
