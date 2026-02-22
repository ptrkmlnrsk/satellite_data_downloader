from src.authorization.auth import authenticate_google_api, initialize_earth_engine
from src.tools.gee_utils import S2Config, S2Downloader
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    credentials = authenticate_google_api()
    initialize_earth_engine(credentials)

    s2_config = S2Config(
        datadir=DATA_DIR,
        collection="COPERNICUS/S2_SR_HARMONIZED",
        scale=10,
        cloud_perc=30,
        bands=["B4", "B3", "B2", "B8"],
        roi_coordinates=[22.229681, 50.554120],
    )

    s2_downloader = S2Downloader(s2_config)

    roi = s2_downloader.build_roi(buffer_m=350)
    img_system_id = s2_downloader.find_image_id(
        roi=roi, start_date="2022-04-01", end_date="2022-05-30"
    )
    scene_metadata = s2_downloader.get_metadata_from_col_id(img_system_id)

    image_id = scene_metadata.get("image_id")

    # todo: niezbyt zoptymalizowane, lepiej by bylo wrzucic ten slownik spowrotem
    # todo: do exportera bo odpytywanie klucza tutaj wygląda żałośnie

    product_id = scene_metadata.get("product_id")
    s2_downloader.export_geotiff(
        image_id=image_id, image_roi=roi, product_id=product_id
    )
