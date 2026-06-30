from src.jobs.finder import Finder
from src.storage.database import db


def main():

    jobs = Finder().search()

    print()

    print(f"Vacantes encontradas: {len(jobs)}")

    print()

    for job in jobs:

        print(job)

        saved = db.save_job(job)

        print("Guardada:", saved)

        print()


if __name__ == "__main__":

    main()