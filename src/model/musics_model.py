from database.database import db
from model.abstract_model import AbstractModel
from pydantic import BaseModel, Field


class CreatedMusic(BaseModel):
    name: str
    artist: str
    album: str
    release_year: int
    gender: str
    image: str


class Music(CreatedMusic):
    id: str = Field(alias="_id")

    def __str__(self):
        return f"{self.name} - {self.artist} ({self.release_year})"


class MusicsModel(AbstractModel[Music]):
    _collection = db["musics"]

    def __init__(self, data: CreatedMusic):
        self.data = data.model_dump()
