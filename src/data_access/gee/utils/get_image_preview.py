from ee import Image
from src.domain.image_request import GEEImageRequest
from src.api.schemas.polygon_model import GEEPolygon


# TODO może zrobić to jako property w klasie GEEImageRequest
def get_image_preview(selected_image: GEEImageRequest) -> str:
    gee_roi = GEEPolygon.from_request(selected_image)
    image = Image(selected_image.image_id).select(selected_image.bands).clip(gee_roi)
    vis_params = {
        "bands": selected_image.bands,  # np. ["B4", "B3", "B2"] dla true color
        "min": 0,
        "max": 3000,
        "dimensions": 512,
        "region": selected_image.roi,
        "format": "png",
    }
    return image.getThumbURL(vis_params)
