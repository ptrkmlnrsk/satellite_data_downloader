from osgeo import gdal
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]

dataset = gdal.Open(
    "D:\\repos\\sentinel_data_downloader\\data\\S2A_MSIL2A_20230928T093031_N0509_R136_T34UEB_20230928T135957.tif",
    gdal.GA_ReadOnly,
)
band = dataset.GetRasterBand(1)
print("Band type ={}".format(gdal.GetDataTypeName(band.DataType)))


scanline = band.ReadRaster(
    xoff=0,
    yoff=0,
    xsize=band.XSize,
    ysize=1,
    buf_xsize=band.XSize,
    buf_ysize=1,
    buf_type=gdal.GDT_Float32,
)
