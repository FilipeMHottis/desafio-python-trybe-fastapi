from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.settings import get_settings

from controller.music_controller import router as music_controller
from controller.render_controller import router as render_controller

settings = get_settings()

app = FastAPI(title=settings.api_name)
app.mount(
    "/static",
    StaticFiles(directory="src/view/static"),
    name="static",
)

app.include_router(music_controller, prefix="/musics", tags=["musics"])
app.include_router(render_controller, tags=["render"])
