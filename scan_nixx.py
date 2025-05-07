import requests
import overpy

latitude = -6.2
longitude = 106.8
radius = 5000

url = "http://overpass-api.de/api/interpreter"

query = f"""
[out:json];
node
    ["amenity"="hospital"]
    (around:{radius},{latitude},{longitude});
out;
"""

response = requests.post(url, data={"data":query})

data = response.json()

print("Daftar Rumah Sakit Terdekat")
for element in data["elements"]:
    name = element["tags"].get("name", "(Tanpa Nama)")
    lat = element["lat"]
    lon = element["lon"]
    print(f"- {name} (Lat: {lat}, Lon: {lon})")
