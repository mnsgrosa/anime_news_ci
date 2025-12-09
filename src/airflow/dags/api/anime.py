import httpx


class AnimeHandler:
    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4"

    def get_today_season(self):
        url = f"{self.base_url}/seasons/now"
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

    def get_upcoming_season(self):
        url = f"{self.base_url}/seasons/upcoming"
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

    def get_anime_by_id(self, anime_id: int):
        url = f"{self.base_url}/anime/{anime_id}"
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
