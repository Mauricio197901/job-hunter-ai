from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/jobhunter.db", echo=False)

print("Base de datos inicializada.")