from dataclasses import dataclass
from datetime import datetime


@dataclass
class Job:

    title: str
    company: str
    location: str
    salary: str
    url: str

    source: str

    description: str = ""

    score: float = 0

    created: datetime = datetime.now()