from src.data_access.gee.image_downloader import GEEImageDownloader
from src.data_access.gee.image_info_service import GEEImageInfoService
from src.data_access.gee.utils.get_metadata import get_gee_metadata_of_image
from src.data_access.gee.utils.get_image_preview import get_image_preview
from src.domain.query import QueryParameters
from src.domain.enums.collections import Collections
from src.domain.image_request import GEEImageRequest
from src.api.schemas.run_request import Sentinel2Request

from fastapi import APIRouter

router = APIRouter()


@router.post("/search")
def search_image(request: Sentinel2Request):  # Pydantic model -> co zwraca endpoint
    collection_enum = Collections(request.collection)

    query_parameters = QueryParameters(  # dataclass -> input usera
        dataset=request.dataset,
        coordinates=request.coordinates,
        collection=collection_enum.value,
        start_date=request.start_date,
        end_date=request.end_date,
        cloud_cover=request.cloud_cover,
        bands=request.bands,
    )
    gee_image_info_service = GEEImageInfoService(query_parameters)
    image_id = gee_image_info_service.get_image_id()
    metadata = get_gee_metadata_of_image(image_id)

    return metadata


@router.post("/preview")
def preview_image(request: GEEImageRequest):
    url = get_image_preview(request)
    return {"preview_url": url}


@router.post("/download")
def download_image(request: GEEImageRequest):
    gee_image_downloader = GEEImageDownloader()
    gee_image_downloader.export_geotiff(request)
