def test_list_musics(client):
    res = client.get("/api/")
    assert res.status_code == 200
    assert res.json == []


def test_create_music(client):
    music_data = {
        "name": "Test Music",
        "artist": "Test Artist",
        "gender": "Test Genre",
        "release_year": 2021,
        "album": "Test Album",
        "image": "https://example.com/image.jpg",
    }
    res = client.post("/api/", json=music_data)
    assert res.status_code == 201, res.json
    assert all(res.json[key] == value for key, value in music_data.items())
    assert res.json["_id"] is not None
