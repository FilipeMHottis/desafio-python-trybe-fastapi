def test_home_page(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "<title>Home</title>" in res.data.decode("utf-8")


def test_home_page_music_cards(client, seed_music):
    res = client.get("/")
    html_text = res.data.decode("utf-8")
    assert res.status_code == 200
    assert seed_music.name in html_text
    assert seed_music.artist in html_text
    assert seed_music.album in html_text
    assert seed_music.image in html_text
    assert str(seed_music.release_year) in html_text

    assert seed_music._id not in html_text
    assert seed_music.gender not in html_text


def test_music_detail_card(client, seed_music):
    res = client.get(f"/{seed_music._id}")
    html_text = res.data.decode("utf-8")

    assert res.status_code == 200
    assert seed_music.name in html_text
    assert seed_music.artist in html_text
    assert seed_music.album in html_text
    assert seed_music.image in html_text
    assert str(seed_music.release_year) in html_text

    assert seed_music._id in html_text
    assert seed_music.gender in html_text
    assert "python é legal" in html_text
