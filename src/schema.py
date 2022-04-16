
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class RestaurantSchema(BaseModel):
    
    id: str
    rating: int
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float
    lng: float

    class Config:
        orm_mode = True




class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class Statistics(BaseModel):
    count: int
    avg: Optional[float]
    std: Optional[float]

    class Config:
        orm_mode = True