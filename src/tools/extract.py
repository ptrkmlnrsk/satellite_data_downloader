
import traceback
from src.authorization.auth import *
from src.tools.gee_utils import get_image, get_metadata, download_image_by_id
from pathlib import Path
import geemap
import ee
import os

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":

    credentials = authenticate_google_api()
    initialize_earth_engine(credentials)

    data_to_find = {
        "roi_coordinates":[22.229681, 50.554120],
        "collection":'COPERNICUS/S2_SR_HARMONIZED',
        "start_date":'2023-09-01',
        "end_date":'2023-10-31',
        "cloud_percentage": 30
    }

    img_id, roi = get_image(coordinates=data_to_find.get('roi_coordinates'),
                            image_collection=data_to_find.get("collection"),
                            start_date=data_to_find.get("start_date"),
                            end_date=data_to_find.get("end_date"),
                            cloud_percentage=data_to_find.get("cloud_percentage"),
                            )

    img_metadata = get_metadata(img_id)
    print(img_metadata)

    #safe_id = img_id.replace("/", "_")
    product_id = img_metadata.get("product_id")
    os.makedirs("data", exist_ok=True)
    target_path = DATA_DIR / f"{product_id}.tif"

    print(f'Selected image id: {img_id}')

    if img_id:
        download_image_by_id(image_id=img_id,
                             output_path=str(target_path),
                             image_roi=roi)
    else:
        print('Image with given parameters has not been found')

