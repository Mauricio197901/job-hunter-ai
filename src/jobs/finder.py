from src.models.job import Job


class Finder:

    def search(self):

        print("Buscando vacantes...")

        return [
            Job(
                title="Administrador Oracle",
                company="Empresa Demo",
                location="Cali",
                salary="$4.500.000",
                url="https://demo.com/job1",
                source="Demo"
            )
        ]