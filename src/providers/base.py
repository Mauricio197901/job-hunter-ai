from abc import ABC, abstractmethod
from typing import List
from src.models.job import Job


class BaseProvider(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def search(self) -> List[Job]:
        ...