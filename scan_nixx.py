import requests
import time

# Area Indonesia secara kasar (bisa diubah lebih luas/sempit)
min_lat = -11.0
max_lat = 6.0
min_lon = 95.0
max_lon = 141.0

# Grid size (dalam derajat), kecil = lebih presisi tapi lebih banyak request
lat_step = 1.0
lon_step = 1.0

radius = 50000  # 50 km radius
overpass_url = "http://overpass-api.de/api/interpreter"

def search_nixx(lat, lon):
    query = f"""
    [out:json][timeout:25];
    node
      ["shop"]
      ["name"~"nixx", i]
      (around:{radius},{lat},{lon});
    out;
    """

    try:
        response = requests.post(overpass_url, data={"data": query})
        data = response.json()
        return data.get("elements", [])
    except Exception as e:
        print(f"⚠️ Gagal di koordinat ({lat},{lon}):", e)
        return []

# Simpan semua hasil
all_results = []

print("Mulai pemindaian seluruh Indonesia...\n")

lat = min_lat
while lat <= max_lat:
    lon = min_lon
    while lon <= max_lon:
        print(f"🔍 Memindai area lat={lat}, lon={lon}")
        results = search_nixx(lat, lon)
        for el in results:
            name = el["tags"].get("name", "(Tanpa Nama)")
            shop_type = el["tags"].get("shop", "-")
            print(f"- {name} [{shop_type}] (Lat: {el['lat']}, Lon: {el['lon']})")
            all_results.append({
                "name": name,
                "shop": shop_type,
                "lat": el["lat"],
                "lon": el["lon"]
            })

        lon += lon_step
        time.sleep(1.0)  # Hindari banned dari Overpass
    lat += lat_step

print(f"\n✅ Total hasil ditemukan: {len(all_results)} toko")
