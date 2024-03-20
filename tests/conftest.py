import pytest
from src.repository import MusicRepository, Music
from src.app import app


@pytest.fixture(autouse=True)
def clear_database_before_each():
    MusicRepository._collection.drop()


@pytest.fixture(autouse=True, scope="session")
def clear_database_after_all():
    yield  # momento de execução do teste

    # após execução do teste
    MusicRepository._collection.drop()


@pytest.fixture
def seed_music():
    music_data = {
        "name": "Test Music",
        "artist": "Test Artist",
        "gender": "Test Genre",
        "release_year": 2021,
        "album": "Test Album",
        "image": "https://example.com/image.jpg",
    }
    return MusicRepository.create(Music(**music_data))


@pytest.fixture
def client():
    return app.test_client()
