
## Application Programming Interface:
API – Application Programming Interface – Two types – Fast API and Rest API.

An application programming interface is a way for two or more computer programs or components to communicate with each other. It is a type of software interface, offering a service to other pieces of software.

### Importance of API
- Standard format input output
- APIs are needed to bring applications together in order to perform a designed function built around sharing data and executing pre-defined processes.

## FAST API:
•	Create folder ned fast api using poetry\
•	Write poetry shell – to activate poetry\
•	To install packages: poetry add fastapi uvicorn httpx httpie requests \
•	Create file main.py in sub folder

Code #1:
```python
From fastapi import FastAPI

app : FastAPI = FastAPI()

# routers 
@app.get('/')
def index():
    return{"Hello":"world1"}

```

Code #2 - Users
```python
From fastapi import FastAPI

app : FastAPI = FastAPI()

#dictionary
users = {"user1":{"name":"Qasim", "email":"m.qasim@gmail.com"}
"user2":{"name":"Dr.Najeed", "email":"drnajeed@gmail,com"}}
# routers 
@app.get('/')
def index():
    return{"Hello":"world1"}

@app.get('/users/')
def fun_users():
    return users
```

---
uvicorn - server of FastAPI
To run file directly - Work on terminal for uvicorn
```
cd ned_fastapi
ls
main.py
uvicorn main:app   #uvicorn filename:routername
```

To run file using poetry
```
cd../
ls
poertry run uvicorn ned_fastapi.main:app --reload
```

---
### Using jupyter notebbok
- Create request.ipynb
```
import requests

res = requests.get("https://localhost:8000)
res
```

```
res.text
```

```
res.status_code
```

---
Client terminal -  on new terminal
```
http localhost:8000/
```

---
### Moc server or Auto documentation 
- localhost:8000/docs
- localhost:8000/docs#/ - for users code

### On Chrome Server
- localhost:8000/users
- loctahost:8000/items/car
- localhost:8000/items/?skip=0&limit=1

### Test Cases
- Create test case in test folder name: test_main.py


```python
from fastapi.testclient import TestClient
from ned_fastapi.main import app

# object
client_app = TestClient(app=app) 
# first app is for parameter and second one is for constructor class

def test_index():
    res = app.get('/')
    assert res.status_code == 200
    asser res.json() == '{"Hello":"world1"}'
```

To run on terminal 
```
pytest
```

## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://fastapi.tiangolo.com/tutorial/first-steps/
