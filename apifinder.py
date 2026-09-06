import json
import urllib.parse
import urllib.request

# Base URL for the assignment API endpoint
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# Set the target location
address = input("Enter location: ")
if len(address) < 1:
    address = "Tufts University"

# Encode query parameters (`q` and `key=42`)
params = {"q": address, "key": 42}
url = serviceurl + urllib.parse.urlencode(params)

print("Retrieving", url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
print(f"Retrieved {len(data)} characters")

# Parse JSON response
try:
    js = json.loads(data)
except Exception:
    js = None

if not js or "features" not in js or len(js["features"]) == 0:
    print("=== Failure To Retrieve ===")
    print(data)
else:
    # Extract the plus_code from the properties dictionary
    plus_code = js["features"][0]["properties"]["plus_code"]
    print("Plus code", plus_code)
