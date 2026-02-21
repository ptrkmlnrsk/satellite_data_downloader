
import traceback
from src.authorization.auth import *
from pathlib import Path
import geemap
import ee
import os

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_image_info(coordinates: list[float]) -> tuple[str, ee.Geometry]:

    roi = ee.Geometry.Point(coordinates).buffer(450).bounds()

    image = (
        ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
        .filterBounds(roi)
        .filterDate('2024-08-01', '2024-10-30')
        .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', 10))
        .sort('CLOUDY_PIXEL_PERCENTAGE')
        .first()
    )
    full_id = image.get('system:id').getInfo()

    return full_id, roi


def download_image_by_id(image_id: str, output_path: str, image_roi: ee.Geometry) -> None:
    image_to_download = ee.Image(image_id).select(['B4', 'B3', 'B2', 'B8']).clip(image_roi)

    print(f'Downloading image... {image_to_download}')

    try:
        geemap.ee_export_image(
            image_to_download,
            filename=output_path,
            scale=10,
            region=image_roi,
            file_per_band=False)

        print('Image has been successfully downloaded to ' + output_path)

    except Exception as e:
        traceback.print_exc()



if __name__ == "__main__":

    credentials = authenticate_google_api()
    initialize_earth_engine(credentials)

    roi_coordinates = [22.229681, 50.554120]

    img_id, roi = get_image_info(roi_coordinates)



    safe_id = img_id.replace("/", "_")
    os.makedirs("data", exist_ok=True)
    target_path = DATA_DIR / f"{safe_id}.tif"

    print(f'Selected image id: {img_id}')

    if img_id:
        download_image_by_id(image_id=img_id,
                             output_path=str(target_path),
                             image_roi=roi)
    else:
        print('Image with given parameters has not been found')

