from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Base schema (common fields)
class UserBase(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100, example="Arvind Eswar")
    email: EmailStr = Field(..., example="arvind@example.com")
    age: int = Field(..., ge=1, le=120, example=24)
    city: Optional[str] = Field(None, max_length=100, example="Bangalore")


# Schema for creating user
class UserCreate(UserBase):
    pass


# Schema for updating user
class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(
        None, min_length=2, max_length=100, example="Updated Name"
    )
    email: Optional[EmailStr] = Field(None, example="updated@example.com")
    age: Optional[int] = Field(None, ge=1, le=120, example=25)
    city: Optional[str] = Field(None, max_length=100, example="Hyderabad")


# Schema for response
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
