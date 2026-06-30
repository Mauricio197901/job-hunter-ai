from src.infrastructure.db.session import SessionLocal, engine
from src.infrastructure.db.models import Job
from src.infrastructure.db.base import Base
from src.infrastructure.browser.playwright_manager import PlaywrightManager
from src.providers.magneto import MagnetoProvider

Base.metadata.create_all(bind=engine)

class JobPipeline:

    def run(self):
        with PlaywrightManager() as page:
            provider = MagnetoProvider(page)
            jobs = provider.search("python")

        db = SessionLocal()

        saved = []

        for j in jobs:
            if db.query(Job).filter(Job.url == j["url"]).first():
                continue

            job = Job(**j)
            db.add(job)
            saved.append(job)

        db.commit()
        db.close()

        return saved