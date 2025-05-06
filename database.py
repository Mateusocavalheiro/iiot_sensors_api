from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://iiot_data_base_user:2RHRLL1F782N3v37qbmW7dBFsagE94Nd@dpg-d0cduv6uk2gs73f787n0-a/iiot_data_base"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()