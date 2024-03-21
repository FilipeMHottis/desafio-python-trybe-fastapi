from database import db

musics_data = [
    {
        "name": "In the End",
        "artist": "Linkin Park",
        "album": "Hybrid Theory",
        "release_year": 2000,
        "gender": "Rock",
        "image": "images/linkin-park.jpeg",
    },
    {
        "name": "Break My Heart",
        "artist": "Dua Lipa",
        "album": "Future Nostalgia",
        "release_year": 2020,
        "gender": "POP",
        "image": "images/dua-lipa.jpeg",
    },
    {
        "name": "You Make Me",
        "artist": "Avicii",
        "album": "True: Avicii By Avicii",
        "release_year": 2014,
        "gender": "Electronic",
        "image": "images/avicii.jpeg",
    },
    {
        "name": "Negro Drama",
        "artist": "Racionais MCs",
        "album": "Nada como um dia após um outro dia",
        "release_year": 2002,
        "gender": "Rap",
        "image": "images/racionais-mcs.jpeg",
    },
    {
        "name": "Mine Mine Mine",
        "artist": "Wind Rose",
        "album": "Wintersaga",
        "release_year": 2019,
        "gender": "Metal",
        "image": "images/wind-rose.jpg",
    },
    {
        "name": "Could You Be Loved",
        "artist": "Bob Marley",
        "album": "Uprising",
        "release_year": 1980,
        "gender": "Reggae",
        "image": "images/bob-marley.jpeg",
    },
]


def run():
    print("Inserindo dados...")

    collection = db["musics"]
    collection.insert_many(musics_data)

    print("Dados inseridos com sucesso!")


if __name__ == "__main__":
    run()
