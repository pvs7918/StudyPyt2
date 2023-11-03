from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Для запуска приложения необходимо использовать сервер для запуска приложений uvicorn.
# Для этого открываем терминал ОС, переходим в каталог с проектом и выполняем следующую команду:
# uvicorn main:app --reload