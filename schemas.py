from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class LeituraBase(BaseModel):
    valor: float
    timestamp: Optional[datetime] = None

class LeituraCreate(LeituraBase):
    valor: float
    timestamp: Optional[datetime] = None

class LeiturasInput(BaseModel):
    leituras: List[LeituraCreate]

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
