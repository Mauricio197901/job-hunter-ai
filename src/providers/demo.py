from src.models.job import Job
from src.providers.base import BaseProvider


class DemoProvider(BaseProvider):
    """
    Proveedor de prueba.
    Más adelante será reemplazado por Magneto, LinkedIn,
    Indeed, Computrabajo, etc.
    """

    @property
    def name(self) -> str:
        return "Demo"

    def search(self) -> list[Job]:
        return [
            Job(
                title="Administrador Oracle",
                company="Banco Demo",
                location="Cali",
                salary="$4.500.000",
                url="https://demo.local/job1",
                source=self.name,
                description="Administración de bases de datos Oracle."
            ),
            Job(
                title="Analista de Ciberseguridad",
                company="Empresa Demo",
                location="Palmira",
                salary="$5.200.000",
                url="https://demo.local/job2",
                source=self.name,
                description="Seguridad informática e infraestructura."
            )
        ]