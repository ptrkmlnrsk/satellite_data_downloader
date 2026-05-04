# from src.api.schemas.download_image import GEEImageDownload

# from src.data_access.gee.gee_service import GEEImageService
# from src.data_access.gee.orchestrator import Orchestrator
from src.data_access.gee.image_downloader import GEEImageDownloader
from src.data_access.gee.image_info_service import GEEImageInfoService
from src.data_access.gee.utils.get_metadata import get_gee_metadata_of_image
from src.domain.query import QueryParameters
from src.domain.enums.collections import Collections
from src.domain.image_request import GEEImageRequest

# from src.api.schemas.download_image import GEEImageDownload
from src.api.schemas.run_request import Sentinel2Request
# from src.domain.polygon import Polygon

from fastapi import APIRouter

router = APIRouter()


@router.post("/search")
def search_image(payload: Sentinel2Request):  # Pydantic model -> co zwraca endpoint
    collection_enum = Collections(payload.collection)

    query_parameters = QueryParameters(  # dataclass -> input usera
        dataset=payload.dataset,
        coordinates=payload.coordinates,
        collection=collection_enum.value,
        start_date=payload.start_date,
        end_date=payload.end_date,
        cloud_cover=payload.cloud_cover,
        bands=payload.bands,
    )
    gee_image_info_service = GEEImageInfoService(query_parameters)
    image_id = gee_image_info_service.get_image_id()
    metadata = get_gee_metadata_of_image(image_id)

    return metadata


@router.post("/download")
def download_image(request: GEEImageRequest):
    # polygon = Polygon(request.roi)
    # polygon.convert_to_gee_roi()

    # image_request = GEEImageRequest(
    #    image_id=request.image_id,
    #    roi=polygon, # rozjebalo mi sie wszystko tu w glowie i nie wiem co powinno byc basemodelem a dataclasa
    #    bands=request.bands,
    # )

    gee_image_downloader = GEEImageDownloader()
    gee_image_downloader.export_geotiff(request)
