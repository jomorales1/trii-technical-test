from fastapi import APIRouter, Depends
from app.utilities.logger import logger
from app.routers.search.models import RickAndMortyParams, RickAndMortyFilters
from app.helpers.ram import get_rick_and_morty_characters

import os
import json
import shutil
import zipfile
import secrets

cd = os.path.dirname(os.path.abspath(__file__))
exports_dir = cd + "/../../public/exports"
router = APIRouter()


@router.get("/search")
async def search(query_params: RickAndMortyParams = Depends()):
    logger.info("Searching for Rick and Morty characters")
    filters = RickAndMortyFilters()
    for key, value in query_params:
        if hasattr(filters, key):
            setattr(filters, key, value)
    response = get_rick_and_morty_characters(page=query_params.page, filters=filters)
    if response.get("error"):
        logger.error(f"Error searching for Rick and Morty characters: {response["message"]}")
    if query_params.generate_zip:
        logger.info("Generating ZIP file")
        # Save results to json file
        token = secrets.token_urlsafe(16)
        os.mkdir(exports_dir + f"/{token}")
        with open(exports_dir + f"/{token}/data.json", "w") as f:
            f.write(json.dumps(response["data"]))
        # Generate ZIP file
        with zipfile.ZipFile(exports_dir + f"/{token}.zip", "w") as zipf:
            zipf.write(exports_dir + f"/{token}/data.json", "data.json", zipfile.ZIP_DEFLATED)
        # Clean up
        shutil.rmtree(exports_dir + f"/{token}")
        response["zip_filename"] = f"{token}.zip"
    return response
