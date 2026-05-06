from pydantic import BaseModel


class ImageResponse(BaseModel):
    image_id: str
    cloud_percentage: float
