# maui_census_puller.py
import requests
import pandas as pd

def get_acs_data(api_key):
    """Fetch ACS 2023 1-Year estimates for Maui County, HI"""
    base_url = "https://api.census.gov/data/2023/acs/acs1"
    
    # Verified 2023 variables from official documentation
    variables = [
        "NAME",
        "B01003_001E",  # Total population
        "B25001_001E",  # Total housing units
        "B25077_001E",  # Median home value (dollars)
        "B25064_001E",  # Median gross rent
        "B19013_001E",  # Median household income
        "B17001_002E"   # Poverty status (under 1.00)
    ]
    
    # Maui County FIPS: state=15 (HI), county=009
    params = {
        'get': ','.join(variables),
        'for': 'county:009',
        'in': 'state:15',
        'key': api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Create DataFrame with proper typing
        df = pd.DataFrame(data[1:], columns=data[0]).apply(pd.to_numeric, errors='ignore')
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e.response.text if e.response else str(e)}")
        return None

def get_tiger_shapefile(geo_type='county', state='15', county='009'):
    """Get TIGER/LINE shapefile for spatial analysis"""
    base_url = "https://www2.census.gov/geo/tiger/TIGER2023"
    url = f"{base_url}/{geo_type.upper()}/tl_2023_{state}_{geo_type}.zip"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(f"tl_2023_{state}_{geo_type}.zip", 'wb') as f:
            f.write(response.content)
        print(f"Downloaded TIGER shapefile for {geo_type} FIPS {state}{county}")
    
    except requests.exceptions.RequestException as e:
        print(f"Shapefile Error: {e}")

if __name__ == "__main__":
    # Get free key: https://api.census.gov/data/key_signup.html
    API_KEY = "YOUR_CENSUS_API_KEY"
    
    # Get ACS data
    acs_data = get_acs_data(API_KEY)
    if acs_data is not None:
        print("\n2023 ACS 1-Year Estimates for Maui County:")
        print(acs_data.drop(columns=['state', 'county']).to_string(index=False))
    
    # Get spatial boundaries
    get_tiger_shapefile()