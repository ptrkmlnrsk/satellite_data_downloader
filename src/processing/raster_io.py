# from typing import Any
import rasterio

# from src.domain.enums.sentinel2_bands import Sentinel2Band


class ReadRaster:
    @staticmethod
    def read_rgb(file_path: str):
        with rasterio.open(file_path) as band:
            return band

    @staticmethod
    def read_nir():
        pass

    @staticmethod
    def read_single_band(*args, **kwargs):
        pass


# def read_raster_bands(file_path: str) -> tuple[Any, Any, Any]:
#    """
#    Read raster bands from a file into separate variables.
#    :param file_path:
#    :return: tuple
#    """
#    with rasterio.open(file_path) as band:
#        green_band = band.read(GREEN_BAND).astype("float32")
#        red_band = band.read(RED_BAND).astype("float32")
#        nir_band = band.read(NIR_BAND).astype("float32")
#
#    return green_band, red_band, nir_band
#
#
# def write_raster():
#    pass
