from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from solution import Customer

engine = create_engine("sqlite:///database.db")
session = sessionmaker(engine)()

customers = session.query(Customer).filter(Customer.name == "Max").all()
print(customers[0])