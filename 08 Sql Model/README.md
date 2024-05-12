## Neon Database
Neon is a fully managed serverless Postgres with a generous free tier. Neon separates storage and compute and offers modern developer features such as serverless, branching, bottomless storage, and more. Neon is open source and written in Rust.
- Sign up neon – create project – in panel create new base – ned – owner username
- Go to dashboard – select ned database – copy connection string 

```
name = "Python"
db_keys = "connection string"
```

- Go to tables – select ned database 
- Go to sql model – https://sqlmodel.tiangolo.com/ - Go to Database to Code (ORMs) – https://sqlmodel.tiangolo.com/db-to-code/ 

### Tutorial – Create a Table
Web: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table-with-db-browser/ 
- Create folder sql model – go to terminal – deactivate panda
Write – poetry new ned_sqlmodel
- cd ned_sqlmodel
- ls
- poetry add sqlmodel fastapi uvicon – installed 
- ls
- Go to vs code – open folder 
- Go to terminal 
- Create a file main.py 
- Select toml file – create new file - .env (use to store important information) 
- Run python ./ned_sqlmodel/main,py


In main.py:
```python
from dotenv import load_dotenv, find-dotenv
import os 

_ : bool = load_dotenv(".env") #read local .env file

print("Hello world!")
print(os.environ.get('name'))
```

In .env file:

```python
name = "Python"
db_keys = "connection string"
# don't forget to write psycorpg2 in connecting key
```

- Create .env_back – as backup file
- Run python ./ned_sqlmodel/main.py

### Connectivity

Create a python file
```python
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
```

### Run python ./ned_sqlmodel/main.py

## Insert data in Table

```python
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
```

### Run python ./ned_sqlmodel/main.py

## Read Data in Table

```python
from dotenv import load_dotenv, find-dotenv
import os 

_ : bool = load_dotenv(".env") #read local .env file

print("Hello world!")
print(os.environ.get('name')) #load variable

from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


# engine = create_engine(str(os.environ.get('db_keys')), echo=True)
engine = create_engine(str(os.environ.get('db_keys')))

SQLModel.metadata.create_all(engine)

obj1 : Hero = Hero()
obj1.name = 'Dr Najeed'
obj1.age = 50
secret_name ="NJ"

obj2: Hero = Hero(name="Qasim", secret_name="SQ". age=30)

with Session(engine) as session:
    session.add(obj1)
    session/add(obj.2)

    session.commit()

def secret_heroes():
    with Session(engine) as session: 
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)

select_heroes()  
```
### Run python ./ned_sqlmodel/main.py