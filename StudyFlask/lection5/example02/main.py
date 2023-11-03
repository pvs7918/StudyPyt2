from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Запуск командой из каталога проекта:
# uvicorn main:app --reload

# Проверка. Перейдите по ссылкам в браузере:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/items/5?q=test