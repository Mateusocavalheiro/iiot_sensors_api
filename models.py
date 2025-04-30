from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Sensor(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, unique=True, index=True)
    tipo = Column(String)
    range_lrv = Column(Float)
    range_urv = Column(Float)

    leituras = relationship("Leitura", back_populates="sensor", cascade="all, delete")

class Leitura(Base):
    __tablename__ = "leituras"

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())  # Agora automático
    sensor_id = Column(Integer, ForeignKey("sensores.id"))

    sensor = relationship("Sensor", back_populates="leituras")
