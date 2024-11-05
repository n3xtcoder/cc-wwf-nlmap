from datetime import datetime

datasets = [{
    "name": "Harmonized Sentinel-2 MSI: MultiSpectral Instrument, Level-1C",
    "description": """
After 2022-01-25, Sentinel-2 scenes with PROCESSING_BASELINE '04.00' or above have their DN (value) range shifted by 1000. The HARMONIZED collection shifts data in newer scenes to be in the same range as in older scenes.

Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as observation of inland waterways and coastal areas.

The Sentinel-2 data contain 13 UINT16 spectral bands representing TOA reflectance scaled by 10000. See the Sentinel-2 User Handbook for details. QA60 is a bitmask band that contained rasterized cloud mask polygons until Feb 2022, when these polygons stopped being produced. Starting in February 2024, legacy-consistent QA60 bands are constructed from the MSK_CLASSI cloud classification bands. For more details, see the full explanation of how cloud masks are computed..
    """,
    "image_id": "COPERNICUS/S2_HARMONIZED",
    "date_start": "2015-06-27",
    "date_end": datetime.now().strftime("%Y-%m-%d"),
    "tags": ["copernicus", "esa", "eu", "msi", "radiance", "sentinel"],
    "is_collection": True,
    "bands": ['B4', 'B3', 'B2'],
    "colors": ["red", "green", "blue"],
    "min": 0,
    "max": 0.3
},
{
    "name": "SRTM Digital Elevation Data Version 4",
    "description": """
The Shuttle Radar Topography Mission (SRTM) digital elevation dataset was originally produced to provide consistent, high-quality elevation data at near global scope. This version of the SRTM digital elevation data has been processed to fill data voids, and to facilitate its ease of use.
    """,
    "image_id": "CGIAR/SRTM90_V4",
    "date_start": "2000-02-11",
    "date_end": "2000-02-22",
    "tags": ["dem", "elevation", "geophysical", "srtm", "topography", "cgiar"],
    "is_collection": False,
    "bands": ["elevation"],
    "colors": ["#000000"],
    "min": 0,
    "max": 5000
},
{
    "name": "Dynamic World V1",
    "image_id": "GOOGLE/DYNAMICWORLD/V1",
    "description": """
Dynamic World is a 10m near-real-time (NRT) Land Use/Land Cover (LULC) dataset that includes class probabilities and label information for nine classes.

Dynamic World predictions are available for the Sentinel-2 L1C collection from 2015-06-27 to present. The revisit frequency of Sentinel-2 is between 2-5 days depending on latitude. Dynamic World predictions are generated for Sentinel-2 L1C images with CLOUDY_PIXEL_PERCENTAGE <= 35%. Predictions are masked to remove clouds and cloud shadows using a combination of S2 Cloud Probability, Cloud Displacement Index, and Directional Distance Transform.

Images in the Dynamic World collection have names matching the individual Sentinel-2 L1C asset names from which they were derived, e.g:

ee.Image('COPERNICUS/S2/20160711T084022_20160711T084751_T35PKT')

has a matching Dynamic World image named: ee.Image('GOOGLE/DYNAMICWORLD/V1/20160711T084022_20160711T084751_T35PKT').

All probability bands except the "label" band collectively sum to 1.

To learn more about the Dynamic World dataset and see examples for generating composites, calculating regional statistics, and working with the time series, see the Introduction to Dynamic World tutorial series.

Given Dynamic World class estimations are derived from single images using a spatial context from a small moving window, top-1 "probabilities" for predicted land covers that are in-part defined by cover over time, like crops, can be comparatively low in the absence of obvious distinguishing features. High-return surfaces in arid climates, sand, sunglint, etc may also exhibit this phenomenon.

To select only pixels that confidently belong to a Dynamic World class, it is recommended to mask Dynamic World outputs by thresholding the estimated "probability" of the top-1 prediction.    
    """,
    "date_start": "2015-06-27",
    "date_end": datetime.now().strftime("%Y-%m-%d"),
    "tags": ["global", "google", "landcover", "landuse", "nrt", "sentinel2-derived"],
    "is_collection": True,
    "bands": ["water","trees","grass","flooded_vegetation","crops","shrub_and_scrub","built","bare","snow_and_ice"],
    "colors": ["#419bdf",  "#397d49",  "#88b053",  "#7a87c6",  "#e49635",  "#dfc35a",  "#c4281b",  "#a59b8f",  "#b39fe1"],
    "min": 0,
    "max": 8
},
{
    "name": "Sentinel-5P OFFL CO: Offline Carbon Monoxide",
    "description": """
OFFL/L3_CO
This dataset provides offline high-resolution imagery of CO concentrations.

Carbon monoxide (CO) is an important atmospheric trace gas for understanding tropospheric chemistry. In certain urban areas, it is a major atmospheric pollutant. Main sources of CO are combustion of fossil fuels, biomass burning, and atmospheric oxidation of methane and other hydrocarbons. Whereas fossil fuel combustion is the main source of CO at northern mid-latitudes, the oxidation of isoprene and biomass burning play an important role in the tropics. TROPOMI on the Sentinel 5 Precursor (S5P) satellite observes the CO global abundance exploiting clear-sky and cloudy-sky Earth radiance measurements in the 2.3 μm spectral range of the shortwave infrared (SWIR) part of the solar spectrum. TROPOMI clear sky observations provide CO total columns with sensitivity to the tropospheric boundary layer. For cloudy atmospheres, the column sensitivity changes according to the light path. More information.

OFFL L3 Product
To make our OFFL L3 products, we find areas within the product's bounding box with data using a command like this:


harpconvert --format hdf5 --hdf5-compression 9
-a 'CO_column_number_density_validity>50;derive(datetime_stop {time})'
S5P_OFFL_L2__CO_____20181031T060643_20181031T074813_05432_01_010200_20181106T052542.nc
grid_info.h5
We then merge all the data into one large mosaic (area-averaging values for pixels that may have different values for different times). From the mosaic, we create a set of tiles containing orthorectified raster data.

Example harpconvert invocation for one tile: harpconvert --format hdf5 --hdf5-compression 9 -a 'CO_column_number_density_validity>50;derive(datetime_stop {time}); bin_spatial(2001, 50.000000, 0.01, 2001, -120.000000, 0.01); keep(CO_column_number_density,H2O_column_number_density,cloud_height, sensor_altitude,sensor_azimuth_angle, sensor_zenith_angle, solar_azimuth_angle,solar_zenith_angle)' S5P_OFFL_L2__CO_____20181031T060643_20181031T074813_05432_01_010200_20181106T052542.nc output.h5

Sentinel-5 Precursor
Sentinel-5 Precursor is a satellite launched on 13 October 2017 by the European Space Agency to monitor air pollution. The onboard sensor is frequently referred to as Tropomi (TROPOspheric Monitoring Instrument).

All of the S5P datasets, except CH4, have two versions: Near Real-Time (NRTI) and Offline (OFFL). CH4 is available as OFFL only. The NRTI assets cover a smaller area than the OFFL assets, but appear more quickly after acquisition. The OFFL assets contain data from a single orbit (which, due to half the earth being dark, contains data only for a single hemisphere).

Because of noise on the data, negative vertical column values are often observed in particular over clean regions or for low SO2 emissions. It is recommended not to filter these values except for outliers, i.e. for vertical columns lower than -0.001 mol/m^2.

The original Sentinel 5P Level 2 (L2) data is binned by time, not by latitude/longitude. To make it possible to ingest the data into Earth Engine, each Sentinel 5P L2 product is converted to L3, keeping a single grid per orbit (that is, no aggregation across products is performed).

Source products spanning the antimeridian are ingested as two Earth Engine assets, with suffixes _1 and _2.

The conversion to L3 is done by the harpconvert tool using the bin_spatial operation. The source data is filtered to remove pixels with QA values less than:

80% for AER_AI
75% for the tropospheric_NO2_column_number_density band of NO2
50% for all other datasets except for O3 and SO2
The O3_TCL product is ingested directly (without running harpconvert).
""",
    "image_id": "COPERNICUS/S5P/OFFL/L3_CO",
    "date_start": "2018-06-28",
    "date_end": datetime.now().strftime("%Y-%m-%d"),
    "tags": ["air-quality", "carbon-monoxide", "copernicus", "esa", "eu", "knmi", "pollution", "s5p", "sentinel", "sron", "tropomi"],
    "is_collection": True,
    "bands": ["CO_column_number_density","H2O_column_number_density","cloud_height","sensor_altitude","sensor_azimuth_angle","sensor_zenith_angle","solar_azimuth_angle"],
    "colors": ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red'],
    "min": 0,
    "max": 0.5
},
{
    "name": "WorldClim BIO Variables V1",
    "description": """
WorldClim V1 Bioclim provides bioclimatic variables that are derived from the monthly temperature and rainfall in order to generate more biologically meaningful values.

The bioclimatic variables represent annual trends (e.g., mean annual temperature, annual precipitation), seasonality (e.g., annual range in temperature and precipitation), and extreme or limiting environmental factors (e.g., temperature of the coldest and warmest month, and precipitation of the wet and dry quarters).

The bands scheme follows that of ANUCLIM, except that for temperature seasonality the standard deviation was used because a coefficient of variation does not make sense with temperatures between -1 and 1.

WorldClim version 1 was developed by Robert J. Hijmans, Susan Cameron, and Juan Parra, at the Museum of Vertebrate Zoology, University of California, Berkeley, in collaboration with Peter Jones and Andrew Jarvis (CIAT), and with Karen Richardson (Rainforest CRC).
""",
    "image_id": "WORLDCLIM/V1/BIO",
    "date_start": "1960-01-01",
    "date_end": "1991-01-01",
    "tags": ["berkeley", "climate", "monthly", "precipitation", "temperature", "weather", "worldclim", "bioclim", "coldest", "diurnal", "driest", "isothermality", "seasonality", "warmest", "wettest"],
    "is_collection": False,
    "bands": ["bio01","bio02","bio03","bio04","bio05","bio06"],
    "colors": ['blue', 'purple', 'cyan', 'green', 'yellow', 'red'],
    "min": -23,
    "max": 30
}]