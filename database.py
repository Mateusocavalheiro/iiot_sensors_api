from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://iiot_data_base_vfvv_user:110TZm9qVhnvMXWWKlTZKlWGGwsr4CPp@dpg-d0dnqgeuk2gs73db1da0-a/iiot_data_base_vfvv"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()