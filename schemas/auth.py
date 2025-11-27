# schemas/auth.py
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # pydantic v1
        # se você estiver usando pydantic v2, pode usar:
        # from_attributes = True  # ainda funciona em modo compat


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
