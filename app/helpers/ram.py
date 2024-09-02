from app.routers.search.models import RickAndMortyFilters
import requests


def get_rick_and_morty_characters(page: int = 1, filters: RickAndMortyFilters = None):
    url = "https://rickandmortyapi.com/api/character/"
    filters = filters.model_dump() if filters else {}
    filters.update({"page": page})
    response = requests.get(url, params=filters)
    if not response.ok:
        return {"status_code": response.status_code, "error": True, "message": response.text}
    return {"status_code": response.status_code, "error": False, "filters": filters, "data": response.json()}