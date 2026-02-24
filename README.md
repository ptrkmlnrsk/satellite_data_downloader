Satellite data ETL. 

Main goal of following project is to download, process and store satellite data, primarly Sentinel 2. 
For now main functions are:
 - downloading Sentinel 2 L2 images from Google Earth Engine, cropped to user defined ROI
 - storage of metadata in PostgreSQL DB

Next steps are: 
 - download parcels from ULDK and make them to be ROI
 - store parcels in DB
 - create processing to calculate basic statistics and remote sensing indices

