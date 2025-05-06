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
    unidade: str
    leituras: Optional[List[LeituraCreate]] = []

class SensorCreate(SensorBase):
    tag: str
    tipo: str
    range_lrv: float
    range_urv: float
    unidade: str
    leituras: List[LeituraCreate] = None
    

class SensorOut(SensorBase):
    id: int
    tag: str
    tipo: str
    range_lrv: float
    range_urv: float
    unidade: str
    #leituras: List[LeituraOut]

    class Config:
        orm_mode = True
