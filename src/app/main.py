from fastapi import FastAPI
from app.settings import get_settings

settings = get_settings()

app = FastAPI(title=settings.api_name)


@app.get("/")
def online_api():
    return {"message": "API is online"}
