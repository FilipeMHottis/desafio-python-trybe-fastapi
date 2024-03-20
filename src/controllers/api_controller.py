from flask import Blueprint, jsonify, request
from repository import MusicRepository, Music

bp = Blueprint("music_api", __name__)


@bp.get("/")
def list_musics():
    return jsonify(MusicRepository.get_all())


@bp.get("/<music_id>")
def get_music(music_id: str):
    try:
        return jsonify(MusicRepository.get_by_id(music_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@bp.post("/")
def create_music():
    try:
        music_instance = Music(**request.json)
    except TypeError as e:
        return jsonify({"error": f"Invalid request: {e}"}), 400
    return jsonify(MusicRepository.create(music_instance)), 201


@bp.delete("/<music_id>")
def delete_music(music_id: str):
    try:
        jsonify(MusicRepository.delete(music_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    else:
        return "", 204
