from fastapi import FastAPI
from app.settings import get_settings

from controller.music_controller import router as music_controller

settings = get_settings()

app = FastAPI(title=settings.api_name)


@app.get("/", tags=["root"])
def online_api():
    return {"message": "API is online"}


app.include_router(music_controller, prefix="/musics", tags=["musics"])
