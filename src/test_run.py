from src.infrastructure.db.session import SessionLocal
from src.infrastructure.db.models import Job
from src.infrastructure.db.base import Base
from src.infrastructure.db.session import engine

Base.metadata.create_all(bind=engine)

db = SessionLocal()

job = Job(
    title="test",
    company="test",
    location="cali",
    url="http://test.com",
    source="manual"
)

db.add(job)
db.commit()

print("OK FUNCIONA:", db.query(Job).count())
db.close()