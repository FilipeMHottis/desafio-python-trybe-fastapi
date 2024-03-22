from model.musics_model import MusicsModel, Music, CreatedMusic
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Music], status_code=200)
def get_all_musics():
    return MusicsModel.get_all()


@router.get("/{id}", response_model=Music, status_code=200)
def get_music(id: str):
    return MusicsModel.get_by_id(id)


@router.post("/", response_model=Music, status_code=201)
def create_music(music: CreatedMusic):
    return MusicsModel(music).save()


@router.put("/{id}", response_model=Music, status_code=200)
def update_music(id: str, music: CreatedMusic):
    return MusicsModel(music).update(id)


@router.delete("/{id}", status_code=204)
def delete_music(id: str):
    return MusicsModel.delete(id)
