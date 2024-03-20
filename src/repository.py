from bson import ObjectId
from database import db
from dataclasses import dataclass


@dataclass
class Music:
    name: str
    artist: str
    album: str
    release_year: int
    gender: str
    image: str


@dataclass
class StoredMusic(Music):
    _id: str

    def __post_init__(self):
        self._id = str(self._id)


class MusicRepository:
    _collection = db["musics"]

    @classmethod
    def get_all(cls) -> list[StoredMusic]:
        return [StoredMusic(**music) for music in cls._collection.find()]

    @classmethod
    def get_by_id(cls, music_id: str) -> StoredMusic:
        music = cls._collection.find_one({"_id": ObjectId(music_id)})
        if music:
            return StoredMusic(**music)
        raise ValueError(f"Music {music_id} not found")

    @classmethod
    def create(cls, data: Music) -> StoredMusic:
        insert_result = cls._collection.insert_one(data.__dict__)
        new_music = cls._collection.find_one(
            {"_id": insert_result.inserted_id}
        )
        return StoredMusic(**new_music)

    @classmethod
    def delete(cls, music_id: str) -> None:
        delete_result = cls._collection.delete_one({"_id": ObjectId(music_id)})
        if delete_result.deleted_count == 0:
            raise ValueError(f"Music {music_id} not found")
