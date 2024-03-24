from abc import ABC
from pymongo.collection import Collection
from bson import ObjectId
from typing import Generic, TypeVar, Dict, List, TypedDict

T = TypeVar("T", bound=Dict)


class DeleteReturn(TypedDict):
    deleted: int


class AbstractModel(ABC, Generic[T]):
    _collection: Collection

    def __init__(self, data: Dict = None):
        self.data = data

    @classmethod
    def validate_id(cls, _id: str) -> bool:
        return ObjectId.is_valid(_id)

    @classmethod
    def get_all(cls) -> List[T]:
        result = cls._collection.find()
        return [
            {
                **item,
                "_id": str(item["_id"]),
            }
            for item in result
        ]

    @classmethod
    def get_by_id(cls, _id: str) -> T:
        if not cls.validate_id(_id):
            raise ValueError("Invalid ID")
        find_returned = cls._collection.find_one({"_id": ObjectId(_id)})
        if not find_returned:
            raise ValueError("ID not found")
        return {
            **find_returned,
            "_id": str(find_returned["_id"]),
        }

    def save(self) -> T:
        saved = self._collection.insert_one(self.data)
        result = self._collection.find_one({"_id": saved.inserted_id})
        return {
            **result,
            "_id": str(result["_id"]),
        }

    def update(self, _id: str) -> T:
        if not self.validate_id(_id):
            raise ValueError("Invalid ID")

        self._collection.update_one(
            {"_id": ObjectId(_id)},
            {"$set": self.data},
        )

        result = self._collection.find_one({"_id": ObjectId(_id)})

        return {
            **result,
            "_id": str(result["_id"]),
        }

    @classmethod
    def delete(cls, _id: str) -> DeleteReturn:
        if not cls.validate_id(_id):
            raise ValueError("Invalid ID")
        cls._collection.delete_one({"_id": ObjectId(_id)})
        return {"msg": "Deleted"}
