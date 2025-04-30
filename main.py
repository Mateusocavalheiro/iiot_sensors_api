from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sensores/", response_model=schemas.SensorOut)
def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    # Checar se já existe tag
    db_sensor = db.query(models.Sensor).filter(models.Sensor.tag == sensor.tag).first()
    if db_sensor:
        raise HTTPException(status_code=400, detail="Sensor com essa tag já existe.")

    new_sensor = models.Sensor(
        tag=sensor.tag,
        tipo=sensor.tipo,
        range_lrv=sensor.range_lrv,
        range_urv=sensor.range_urv
    )
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)

    # Adicionar leituras
    for leitura in sensor.leituras:
        new_leitura = models.Leitura(
            valor=leitura.valor,
            timestamp=leitura.timestamp if leitura.timestamp else datetime.utcnow(),
            sensor_id=new_sensor.id
        )
        db.add(new_leitura)

    db.commit()
    db.refresh(new_sensor)

    return new_sensor

@app.get("/sensores/", response_model=List[schemas.SensorOut])
def list_sensores(db: Session = Depends(get_db)):
    sensores = db.query(models.Sensor).all()
    return sensores

# Buscar todas as leituras de um sensor por intervalo de datas
from typing import Optional
from datetime import datetime

@app.get("/leituras/{sensor_id}", response_model=List[schemas.LeituraOut])
def get_leituras(sensor_id: int, start: Optional[datetime] = None, end: Optional[datetime] = None, db: Session = Depends(get_db)):
    query = db.query(models.Leitura).filter(models.Leitura.sensor_id == sensor_id)
    
    if start:
        query = query.filter(models.Leitura.timestamp >= start)
    if end:
        query = query.filter(models.Leitura.timestamp <= end)
    
    leituras = query.all()
    return leituras
