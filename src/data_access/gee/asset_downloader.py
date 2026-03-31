# from ee import Image
# from traceback import print_exc
# from geemap import ee_export_image
# from src.data_access.domain.query import QueryParameters
#
# from src.tools.constants import DATA_DIR


# class SatelliteImageDownloader:
#    def __init__(self, query_params: QueryParameters) -> None:
#        self.query_params = query_params
#
#    def export_geotiff(self) -> None:
#        # bands
#        image_to_download = (
#            Image(image_id).select(self.query_params.bands).clip(image_roi) # F821
#        )
#
#        safe_id = product_id.replace("/", "_")
#        output_name = DATA_DIR / f"{safe_id}.tif"
#
#        print(f"Downloading image... {image_to_download}")
#
#        try:
#            ee_export_image(
#                image_to_download,
#                filename=str(output_name),
#                scale=10,
#                region=image_roi,
#                file_per_band=False,
#            )
#
#            print("Image has been successfully downloaded to ", DATA_DIR)
#
#        except Exception:
#            print_exc()
