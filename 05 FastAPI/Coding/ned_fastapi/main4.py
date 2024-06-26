from fastapi import FastAPI


app : FastAPI = FastAPI()


@app.get('/')
def index():
    return {"Hello": "world1"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]




