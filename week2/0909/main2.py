from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI 간단한 CRUD API")

# pydantic 모델 정의
class ItemSchema(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

# 메모리 데이터베이스
items_db: dict[int, dict] = {}

# Create: 데이터 생성
@app.post("/items/", status_code=201)
async def create_item(item: ItemSchema):
    new_id = max(items_db.keys(), default=0) + 1
    new_item = {"id": new_id, **item.model_dump()}
    items_db[new_id] = new_item
    return {"message": "아이템이 성공적으로 생성되었습니다.", "data": new_item}

# Read: 전체 조회
# http://127.0.0.1:8000/items/
@app.get("/items/")
async def read_all_items():
    return {"total": len(items_db), "data": list(items_db.values())}

# Read: 단일 조회
# http://127.0.0.1:8000/items/{int}
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")
    return {"data": items_db[item_id]}

# Update: 데이터 전체 수정
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemSchema):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

    updated_item = {"id": item_id, **item.model_dump()}
    items_db[item_id] = updated_item
    return {"message": "수정 완료", "data": updated_item}

# Delete: 데이터 삭제
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

    deleted_item = items_db.pop(item_id)
    return {"message": "아이템이 성공적으로 삭제되었습니다.", "deleted_data": deleted_item}
