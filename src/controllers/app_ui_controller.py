from flask import Blueprint, render_template
from repository import MusicRepository


bp = Blueprint("music_app_ui", __name__)


@bp.errorhandler(ValueError)
def handle_value_error(e):
    return render_template("error_page.html", error_msg=e), 404


@bp.get("/")
def home():
    all_musics = MusicRepository.get_all()
    return render_template("home.html", musics=all_musics)


@bp.get("/<music_id>")
def music_detail(music_id: str):
    found_music = MusicRepository.get_by_id(music_id)
    return render_template("music_detail.html", music=found_music)
