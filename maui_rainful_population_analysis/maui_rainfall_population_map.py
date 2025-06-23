import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import zipfile
import os

# --- 1. Download and extract Maui census tract shapefile ---
tiger_url = "https://www2.census.gov/geo/tiger/TIGER2023/TRACT/tl_2023_15_tract.zip"
shapefile_zip = "tl_2023_15_tract.zip"
shapefile_dir = "tl_2023_15_tract"

if not os.path.exists(shapefile_dir):
    r = requests.get(tiger_url)
    with open(shapefile_zip, 'wb') as f:
        f.write(r.content)
    with zipfile.ZipFile(shapefile_zip, 'r') as zip_ref:
        zip_ref.extractall(shapefile_dir)

tracts = gpd.read_file(os.path.join(shapefile_dir, 'tl_2023_15_tract.shp'))

# --- 2. Fetch ACS 2023 1-Year population data for Maui tracts ---
API_KEY = "8c50345a791508c9286af54259245077f6e48c62"
acs_url = f"https://api.census.gov/data/2023/acs/acs1?get=NAME,B01003_001E&for=tract:*&in=state:15+county:009&key={API_KEY}"
response = requests.get(acs_url)
data = response.json()
census_df = pd.DataFrame(data[1:], columns=data[0])
census_df['GEOID'] = census_df['state'] + census_df['county'] + census_df['tract']

# Merge census data with tracts
tracts = tracts.merge(census_df[['GEOID', 'B01003_001E']], on='GEOID', how='left')
tracts['B01003_001E'] = pd.to_numeric(tracts['B01003_001E'])

# --- 3. Read and process rainfall CSV ---
rain = pd.read_csv('maui_rainfall.csv')

# Clean up column names if needed (remove quotes)
rain.columns = [c.replace('"', '').strip() for c in rain.columns]

# Convert PRCP to numeric (remove any attributes column if present)
rain['PRCP'] = pd.to_numeric(rain['PRCP'], errors='coerce')
rain = rain.dropna(subset=['LATITUDE', 'LONGITUDE', 'PRCP'])

# rain = rain[rain['DATE'] == '2024-01']

# Convert to GeoDataFrame
rain_gdf = gpd.GeoDataFrame(
    rain,
    geometry=gpd.points_from_xy(rain['LONGITUDE'], rain['LATITUDE']),
    crs='EPSG:4326'
)

# --- 4. Plot the map ---
fig, ax = plt.subplots(figsize=(12, 10))
tracts.plot(
    column='B01003_001E',
    cmap='Blues',
    linewidth=0.8,
    ax=ax,
    edgecolor='0.8',
    legend=True,
    legend_kwds={'label': "Population by Tract"}
)
rain_gdf.plot(
    ax=ax,
    color='red',
    markersize=rain_gdf['PRCP'] * 2,  # Adjust multiplier for visibility
    alpha=0.7,
    label='Rainfall (size = amount)'
)
plt.title('Maui Population by Census Tract and Rainfall Stations')
plt.axis('off')
plt.legend()
plt.show()