from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class LeituraBase(BaseModel):
    valor: float
    timestamp: datetime

class LeituraCreate(LeituraBase):
    pass

class LeituraOut(LeituraBase):
    id: int

    class Config:
        orm_mode = True

class SensorBase(BaseModel):
    tag: str
    tipo: str
    range_lrv: float
    range_urv: float

class SensorCreate(SensorBase):
    leituras: List[LeituraCreate]

class SensorOut(SensorBase):
    id: int
    leituras: List[LeituraOut]

    class Config:
        orm_mode = True
