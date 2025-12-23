# Resources and Data Sources for Maui Rainfall and Flood Analysis

This document lists the main data sources and tools used for precipitation analysis and remote sensing in the Maui Rainfall and Flood Analysis project. Each resource includes a brief description and a direct link.

---

## Precipitation Data

- **MesoWest Hawaii**
  - [MesoWest Hawaii Map](https://mesowest.utah.edu/cgi-bin/droman/mesomap.cgi?state=HI&rawsflag=3)
  - Real-time and historical weather station data for Hawaii, including rainfall. Select Maui stations, view recent rain totals, and download CSVs for analysis.

- **NOAA National Centers for Environmental Information (NCEI)**
  - [NOAA NCEI Data Access](https://www.ncei.noaa.gov/access)
  - Official archive for U.S. climate and weather data, including daily and hourly precipitation records. Data can be accessed via web interface or API.

- **National Weather Service (NWS) Precipitation**
  - [NWS Daily Precipitation](https://www.weather.gov/marfc/DailyPrecipitation)
  - Daily precipitation reports from the National Weather Service. For Hawaii, use the Honolulu WFO for local data.

---

## Remote Sensing Data

- **Landsat Imagery**
  - [Landsat Band Combination Tool](https://landsat.gsfc.nasa.gov/apps/bandcombination/)
  - Visualize and select band combinations for Landsat imagery (e.g., for NDWI/NDVI analysis). Download images from USGS Earth Explorer or similar portals.

- **MODIS Imagery**
  - [MODIS Home](https://modis.gsfc.nasa.gov)
  - MODIS provides near-daily global imagery for vegetation, surface reflectance, and water mapping. Data available for download and analysis.

---

## Google Earth Engine Datasets

- **MODIS in Earth Engine**
  - [Earth Engine MODIS Datasets](https://developers.google.com/earth-engine/datasets/catalog/modis)
  - Access MODIS surface reflectance, land cover, and water products directly in Google Earth Engine for cloud-based analysis.

- **Landsat in Earth Engine**
  - [Earth Engine Landsat Datasets](https://developers.google.com/earth-engine/datasets/catalog/landsat)
  - Access all Landsat missions and process imagery for NDWI, NDVI, and change detection in Google Earth Engine.

---

## Additional Resources

- **Rainfall Atlas of Hawaiʻi**
  - [Rainfall Atlas](https://www.hawaii.edu/climate-data-portal/rainfall-atlas/)
  - High-resolution, gridded rainfall climatology for the Hawaiian Islands, useful for spatial context and validation.

- **Google Earth Engine Python API**
  - [Earth Engine Python Install Guide](https://developers.google.com/earth-engine/python_install)
  - Instructions for installing and using the Earth Engine Python API for remote sensing analysis.

---

## How to Use These Resources

- Download precipitation data (CSV or API) for Maui for the event period.
- Download or process Landsat and MODIS imagery for Maui before and after the January 2024 rainstorm.
- Use Google Earth Engine for advanced, cloud-based analysis and visualization.
- Reference the Rainfall Atlas for long-term rainfall patterns.