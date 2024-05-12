from dotenv import load_dotenv, find-dotenv
import os 

_ : bool = load_dotenv(".env") #read local .env file

print("Hello world!")
print(os.environ.get('name')) #load variable

from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


engine = create_engine(str(os.environ.get('db_keys')), echo=True)

SQLModel.metadata.create_all(engine)

obj1 : Hero = Hero()
obj1.name = 'Dr Najeed'
obj1.age = 50

obj2: Hero = Hero(name="Qasim", secret_name="SQ". age=30)

with Session(engine) as session:
    session.add(obj1)
    session/add(obj.2)

    session.commit()

    