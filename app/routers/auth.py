from fastapi import APIRouter
from app.schemas.user import UserCreate
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate
router = APIRouter()

@router.get("/test")
def test():
  return {"message": "Auth router works"}

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered successfully"}
