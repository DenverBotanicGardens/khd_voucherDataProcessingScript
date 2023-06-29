import requests
import urllib
import pandas as pd

# USGS Elevation Point Query Service
#url = r'https://nationalmap.gov/epqs/pqs.php?'
#new 2023:
url = r'https://epqs.nationalmap.gov/v1/json?'

# coordinates with known elevation 
lat = [48.633, 48.733, 45.1947, 45.1962]
lon = [-93.9667, -94.6167, -93.3257, -93.2755]
   
# create data frame
df = pd.DataFrame({
    'lat': lat,
    'lon': lon
})

def elevation_function(df, lat_column, lon_column):
    """Query service using lat, lon. add the elevation values as a new column."""
    elevations = []
    for lat, lon in zip(df[lat_column], df[lon_column]):
                
        # define rest query params
        params = {
            'output': 'json',
            'x': lon,
            'y': lat,
            'units': 'Meters'
        }
        
        # format query string and return query value
        result = requests.get((url + urllib.parse.urlencode(params)))
        #elevations.append(result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])
        #new 2023:
        print(result.json()['value'])
        elevations.append(result.json()['value'])

    df['elev_meters'] = elevations

elevation_function(df, 'lat', 'lon')
# print(df.head())
    