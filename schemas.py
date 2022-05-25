from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserInDBBase(UserBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


class AddressBase(BaseModel):
    title: str
    author: str
    published: int


class AddressCreate(AddressBase):
    is_active: Optional[bool] = True


class AddressInDBBase(AddressBase):
    id: str

    class Config:
        orm_mode = True


