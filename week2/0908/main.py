from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_naem": "Baz"}]

# http://localhost:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://localhost:8000/items/{int}
# http://localhost:8000/items/{int}?q={str}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# http://localhost:8000/users/me
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# http://localhost:8000/users/{str}
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return{"user_id": user_id}

# http://localhost:8000/users
@app.get("/users")
async def read_users():
    return["Rick", "Morty"]

# http://localhost:8000/users (무시됨)
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# http://localhost:8000/models/{alexnet}
# http://localhost:8000/models/{resnet}
# http://localhost:8000/models/{lenet}
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):

    # 키를 요청해서, 값을 비교
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW!"}

    # 값을 요청해서, 값을 비교
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    # 그 외에 상황
    return {"model_name": model_name, "message": "Have some residuals"}

# http://localhost:8000/items/
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
 
# http://localhost:8000/items2/{str}
# http://localhost:8000/items2/{str}?q={str}
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

