import requests

latitude = -6.2
longitude = 106.8
radius = 5000

url = "http://overpass-api.de/api/interpreter"

query = f"""
[out:json];
node
  ["shop"~"vape|convenience|electronics"]
  ["name"~"nixx", i]
  (around:{radius},{latitude},{longitude});
out;
"""

response = requests.post(url, data={"data": query})
data = response.json()

print("Toko dengan nama mengandung 'NIXX':")
for element in data["elements"]:
    name = element["tags"].get("name", "(Tanpa Nama)")
    lat = element["lat"]
    lon = element["lon"]
    print(f"- {name} (Lat: {lat}, Lon: {lon})")
  
