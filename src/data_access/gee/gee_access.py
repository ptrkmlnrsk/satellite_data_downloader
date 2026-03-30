from ee import Geometry, ImageCollection, Filter, Image
from datetime import datetime, timezone
from src.config import CLOUDY_PIXEL_PERCENTAGE


class AssetInfoObtainer:
    def __init__(self, collection):
        self.collection = collection
        self.image_system_id: str | None = None

    def get_image_id(self, roi: Geometry, start_date: str, end_date: str) -> None:
        """
        Get image system id
        within date range. Selected system id
        is id of first top image sorted within date range
        based on max cloud percentage.
        Sets GEE system id of image.
        """

        collection = (
            ImageCollection(self.collection)
            .filterBounds(roi)
            .filterDate(start_date, end_date)
            .filter(Filter.lte("CLOUDY_PIXEL_PERCENTAGE", CLOUDY_PIXEL_PERCENTAGE))
        )

        if collection.size().getInfo() == 0:
            raise Exception("Invalid collection")

        img = collection.sort("CLOUDY_PIXEL_PERCENTAGE").first()

        self.image_system_id = img.get("system:id").getInfo()

    def get_metadata_of_image(self) -> dict[str, str]:
        """
        Extracts particular metadata of image to a dictionary.
        :return: dictionary
        """
        img = Image(self.image_system_id)
        metadata = img.toDictionary().getInfo()

        acquired_at = datetime.fromtimestamp(
            metadata.get("GENERATION_TIME") / 1000, tz=timezone.utc
        ).isoformat()

        return {
            "image_id": self.image_system_id,
            "product_id": metadata.get("PRODUCT_ID"),
            "acquired_at": acquired_at,
            "cloud_pct": metadata.get("CLOUDY_PIXEL_PERCENTAGE"),
            "mgrs_tile": metadata.get("MGRS_TILE"),
            "platform": metadata.get("SPACECRAFT_NAME"),
            "processing_baseline": metadata.get("PROCESSING_BASELINE"),
            "processing_level": metadata.get("PROCESSING_LEVEL"),
            "product_type": metadata.get("PRODUCT_TYPE"),
        }
