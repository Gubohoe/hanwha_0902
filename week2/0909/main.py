from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class ItemUpdate(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

item_db={
    1: {"name": "노트북", "price": 1200000},
    2: {"name": "스마트폰", "price": 800000},
    3: {"name": "마우스", "price": 30000}
}
item_db2={
    1: {"name": "노트북", "price": 1200000, "is_offer": True},
    2: {"name": "스마트폰", "price": 800000, "is_offer": False}
}


app = FastAPI()


# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/users/{str}
@app.get("/users/{user_id}")
async def users(user_id: str):
    return {"message":"Hello "+user_id}


# http://127.0.0.1:8000/items/{int}
@app.get("/items/{item_id}")
async def user(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/items/
@app.post("/items/")
async def create_item(item: Item):
    total_price = item.price * 1.1
    return {
        "message": "아이템이 성공적으로 생성되었습니다.",
        "data": item,
        "price_with_tax": round(total_price, 2)
    }

# http://127.0.0.1:8000/items/
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    # 찾는 상품이 없을 경우
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="해당 아이템을 찾을 수 없습니다.")

    # 삭제된 아이템
    deleted_item = item_db.pop(item_id)

    return {
        "message": f"ID {item_id} 아이템이 삭제되었습니다.",
        "deleted_data": deleted_item
    }

# http://127.0.0.1:8000/items
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemUpdate):
    # 찾는 상품이 없을 때
    if item_id not in item_db2:
        raise HTTPException(status_code=404, detail="해당 아이템을 찾을 수 없습니다.")

    item_db2[item_id] = item.model_dump()

    return{
        "message": f"ID {item_id} 아이템이 성공적으로 수정되었습니다.",
        "data": item_db2[item_id]
    }