from typing import List

from fastapi import APIRouter, Depends
from fastapi_redis_cache import cache
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import func

from db import get_db
from cache import redis_client
import constants as const
import models
import schemas

api_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


@api_router.get('/list/users', response_model=List[schemas.UserInDBBase])
def list_user(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
):
    res = db.query(models.User).offset(skip).limit(limit).all()
    return res


@api_router.post('/create/user')
def create_user(
        obj_in: schemas.UserCreate,
        db: Session = Depends(get_db),
):
    db_obj = models.User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
        full_name=obj_in.full_name,
    )
    db.add(db_obj)
    db.commit()

    return 'successfully created'


@api_router.get('/view/address', response_model=List[schemas.AddressInDBBase])
@cache()
def list_book(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
):
    res = db.query(models.Address).offset(skip).limit(limit).all()

    return res


@api_router.post('/create/address')
def create_address(
        obj_in: schemas.AddressCreate,
        db: Session = Depends(get_db),
):
    db_obj = models.Address(
        houseno=obj_in.houseno,
        area=obj_in.area,
        city=obj_in.city,
        state=obj_in.state,
        pincode=obj_in.pincode,
        latitude=obj_in.latitude,
        longitude=obj_in.longitude,
    )
    db.add(db_obj)
    db.commit()

    return 'successfully created'


@api_router.put('/update/address')
def update_address(
        updated_house_no: str
):
    db_obj = models.Address(
        houseno=updated_house_no
    )
    db.add(db_obj)
    db.commit()

    return 'successfully updated'



@api_router.delete('/delete/address')
def delete_address(
        obj_in: schemas.AddressBase,
        db: Session = Depends(get_db),
):
    res = db.query(models.Address).remove(id).all()

    return 'successfully deleted'




