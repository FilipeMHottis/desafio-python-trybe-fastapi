from model.musics_model import MusicsModel, Music, CreatedMusic
from fastapi import APIRouter, HTTPException
from typing import List, TypedDict

router = APIRouter()


class ErrorDictType(TypedDict):
    status: int
    msg: str


def error_return(e: ValueError) -> ErrorDictType:
    if e == "Invalid ID":
        return {"status": 400, "msg": str(e)}

    return {"status": 404, "msg": str(e)}


@router.get("/", response_model=List[Music], status_code=200)
def get_all_musics():
    return MusicsModel.get_all()


@router.get("/{id}", response_model=Music, status_code=200)
def get_music(id: str):
    try:
        return MusicsModel.get_by_id(id)
    except ValueError as e:
        error = error_return(e)
        raise HTTPException(status_code=error["status"], detail=error["msg"])


@router.post("/", response_model=Music, status_code=201)
def create_music(music: CreatedMusic):
    try:
        return MusicsModel(music).save()
    except ValueError as e:
        error = error_return(e)
        raise HTTPException(status_code=error["status"], detail=error["msg"])


@router.put("/{id}", response_model=Music, status_code=200)
def update_music(id: str, music: CreatedMusic):
    try:
        return MusicsModel(music).update(id)
    except ValueError as e:
        error = error_return(e)
        raise HTTPException(status_code=error["status"], detail=error["msg"])


@router.delete("/{id}", status_code=204)
def delete_music(id: str):
    try:
        return MusicsModel.delete(id)
    except ValueError as e:
        error = error_return(e)
        raise HTTPException(status_code=error["status"], detail=error["msg"])
