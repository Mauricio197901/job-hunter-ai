from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from .base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    url = Column(String, unique=True)
    source = Column(String)
    score = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)