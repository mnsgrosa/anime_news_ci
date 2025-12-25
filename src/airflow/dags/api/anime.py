import httpx
from constants import BASE_URL


def get_today_season():
    url = f"{BASE_URL}/seasons/now"
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
    data = response.json()

    data_dictionary = {
        "mal_id": data.get("mal_id", []),
        "url": data.get("url", []),
        "titles": data.get("titles", []),
        "episodes": data.get("episodes", []),
        "airing": data.get("airing", []),
        "duration": data.get("duration", []),
        "studios": data.get("studios", []),
        "genres": data.get("genres", []),
        "themes": data.get("themes", []),
        "synopsis": data.get("synopsis", []),
    }

    return data_dictionary


def get_upcoming_season():
    url = f"{BASE_URL}/seasons/upcoming"
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
    data = response.json()

    data_dictionary = {
        "mal_id": data.get("mal_id", []),
        "titles": data.get("titles", []),
        "episodes": data.get("episodes", []),
        "airing": data.get("airing", []),
        "duration": data.get("duration", []),
        "studios": data.get("studios", []),
        "genres": data.get("genres", []),
        "themes": data.get("themes", []),
        "synopsis": data.get("synopsis", []),
    }

    return data_dictionary


def get_anime_by_id(anime_id: int):
    url = f"{BASE_URL}/anime/{anime_id}"
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
    data = response.json()

    data_dictionary = {
        "mal_id": data.get("mal_id", []),
        "titles": data.get("titles", []),
        "episodes": data.get("episodes", []),
        "airing": data.get("airing", []),
        "duration": data.get("duration", []),
        "studios": data.get("studios", []),
        "genres": data.get("genres", []),
        "themes": data.get("themes", []),
        "synopsis": data.get("synopsis", []),
    }

    return data_dictionary
