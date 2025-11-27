from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from models.coin import OriginalityEnum


class CoinBase(BaseModel):
    year: int = Field(..., example=1994)
    country: str = Field(..., example="Brasil")
    face_value: str = Field(..., example="1 Real")
    purchase_price: Optional[float] = Field(None, example=10.5)
    estimated_value: Optional[float] = Field(None, example=25.0)
    originality: OriginalityEnum = Field(OriginalityEnum.original)
    condition: Optional[str] = Field(None, example="Flor de Cunho")
    storage_location: Optional[str] = Field(None, example="Álbum 1, página 3")
    category: Optional[str] = Field(None, example="Comemorativa")
    acquisition_date: Optional[datetime] = Field(None)
    acquisition_source: Optional[str] = Field(None, example="avô")
    notes: Optional[str] = Field(None, example="Moeda rara da copa do mundo")
    image_url_front: Optional[str] = None
    image_url_back: Optional[str] = None


class CoinCreate(CoinBase):
    pass


class CoinUpdate(BaseModel):
    year: Optional[int] = None
    country: Optional[str] = None
    face_value: Optional[str] = None
    purchase_price: Optional[float] = None
    estimated_value: Optional[float] = None
    originality: Optional[OriginalityEnum] = None
    condition: Optional[str] = None
    storage_location: Optional[str] = None
    category: Optional[str] = None
    acquisition_date: Optional[datetime] = None
    acquisition_source: Optional[str] = None
    notes: Optional[str] = None
    image_url_front: Optional[str] = None
    image_url_back: Optional[str] = None


class CoinRead(CoinBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
