from enum import Enum


class Sentinel2Band(Enum):
    """
    Represents Sentinel-2 spectral bands with unique codes and resolutions.

    This Enum provides a structure for various Sentinel-2 bands, including their unique band
    codes and spatial resolutions. It includes utility methods for filtering bands with a
    resolution of 10 meters and for retrieving enum members based on their band codes or names.

    :ivar code: The distinctive code associated with the band.
    :type code: str
    :ivar resolution: Spatial resolution of the band in meters.
    :type resolution: int
    """

    BLUE = ("B2", 10)
    GREEN = ("B3", 10)
    RED = ("B4", 10)
    RED_EDGE = ("B5", 20)
    RED_EDGE_2 = ("B6", 20)
    RED_EDGE_3 = ("B7", 20)
    NIR = ("B8", 10)
    RED_EDGE_4 = ("B8A", 20)
    WATER_VAPOUR = ("B9", 60)
    CIRRUS = ("B10", 60)
    SWIR_1 = ("B11", 20)
    SWIR_2 = ("B12", 20)

    def __init__(self, code: str, resolution: int):
        self.code = code
        self.resolution = resolution

    @property
    def is_10m(self):
        """Checks if band is 10m resolution."""
        return self.resolution == 10

    @classmethod
    def list_bands(cls) -> list[tuple[str, int]]:
        return [band.value for band in cls]

    @classmethod
    def bands_10m(cls):
        """Returns list of bands with 10 m resolution."""
        return [band for band in cls if band.is_10m]

    @classmethod
    def from_any(cls, value: str):
        """Checks if a provided band is in Sentinel2Band Enum and returns it."""
        if value in cls.__members__:  # lista nazw Blue, green itd.
            return cls[value]
        for band in cls:
            if band.code == value:
                return band
        raise ValueError(f"Invalid Sentinel 2 band: {value}")
