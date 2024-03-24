from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from model.musics_model import Music, MusicsModel
from typing import List

router = APIRouter()
templates = Jinja2Templates(directory="src/view/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    try:
        all_musics: List[Music] = MusicsModel.get_all()
        return templates.TemplateResponse(
            "home.html",
            {
                "request": request,
                "musics": all_musics,
            },
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "error_page.html",
            {
                "request": request,
                "error_msg": e,
            },
        )


@router.get("/{music_id}", response_class=HTMLResponse)
def detail(request: Request, music_id: str):
    try:
        music: Music = MusicsModel.get_by_id(music_id)
        return templates.TemplateResponse(
            "music_detail.html",
            {
                "request": request,
                "music": music,
            },
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "error_page.html",
            {
                "request": request,
                "error_msg": e,
            },
        )
