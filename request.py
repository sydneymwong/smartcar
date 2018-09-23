import smartcar
import pandas as pd
from sodapy import Socrata

access_token = 'dd8dda3b-1b20-46c9-bb94-ce84f7a6c70e'

response = smartcar.get_vehicle_ids(access_token)

vid = response['vehicles'][0]

vehicle = smartcar.Vehicle(vid, access_token)

location = vehicle.location()

print(location)

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.sfgov.org", None)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("cuks-n6tp", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

