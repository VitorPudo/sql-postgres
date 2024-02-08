from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Pets(Base):
    __tablename__ = "Pets"

    pet_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String)
    age = Column(Integer, nullable=False)
    owner = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)