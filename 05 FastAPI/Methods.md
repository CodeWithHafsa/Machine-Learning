## Methods to deal with API

- POST
- GET
- PUT
- DELETE

Asynchronized function \
Sunchronized function

---
Case # 1:
```python
From fastapi import FastAPI

app : FastAPI = FastAPI()

# routers 
@app.get('/')
def index():
    return{"Hello":"world1"}

@app.get('/items/{name}')
def fn_items(name):
    return {"purchase item":name} #query parameter
```

Case # 2:
```python
From fastapi import FastAPI

app : FastAPI = FastAPI()

# routers 
@app.get('/')
def index():
    return{"Hello":"world1"}

#query parameter
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

Case # 3:
```python
# Request Body
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get('/')
def index():
    return{"Hello":"world1"}

@app.post("/items/")
async def create_item(item: Item):
    return item
```