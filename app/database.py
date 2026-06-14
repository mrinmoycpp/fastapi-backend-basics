from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Database connected successfully!")
    except Exception as e:
        print("Connection failed!")
        print(e)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

        