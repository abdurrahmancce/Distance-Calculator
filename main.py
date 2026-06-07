import tkinter as tk
from geopy.distance import geodesic
import threading
import time
import requests

# Window Setup
root = tk.Tk()
root.title("Distance Between Two Cities")
root.geometry("560x490")
root.config(bg="#121212")
root.resizable(False, False)

CITY_COORDS = {
    # Bangladesh: 8 Divisions 
    "dhaka":              (23.7104, 90.4074),
    "chittagong":         (22.3384, 91.8317),
    "chattogram":         (22.3384, 91.8317),
    "sylhet":             (24.8990, 91.8720),   # verified: 199 km from Dhaka ✓
    "rajshahi":           (24.3745, 88.6042),
    "khulna":             (22.8456, 89.5403),
    "barisal":            (22.7010, 90.3535),
    "mymensingh":         (24.7471, 90.4203),
    "rangpur":            (25.7439, 89.2752),

    # Dhaka Division
    "narayanganj":        (23.6238, 90.5000),
    "gazipur":            (23.9999, 90.4203),
    "narsingdi":          (23.9200, 90.7153),
    "manikganj":          (23.8634, 90.0007),
    "munshiganj":         (23.5422, 90.5300),
    "madaripur":          (23.1624, 90.2007),
    "shariatpur":         (23.2423, 90.4348),
    "faridpur":           (23.5983, 89.8350),
    "gopalganj":          (23.0050, 89.8266),
    "rajbari":            (23.7572, 89.6441),
    "tangail":            (24.2513, 89.9167),
    "kishoreganj":        (24.4449, 90.7766),
    "netrokona":          (24.8703, 90.7279),
    "jamalpur":           (24.9378, 89.9378),
    "sherpur":            (25.0194, 90.0159),

    # Chittagong Division
    "cox's bazar":        (21.4539, 91.9677),   # verified
    "coxs bazar":         (21.4539, 91.9677),
    "cox bazar":          (21.4539, 91.9677),
    "feni":               (23.0144, 91.3966),   # verified: 127 km from Dhaka ✓
    "comilla":            (23.4619, 91.1850),   # verified: 84 km from Dhaka ✓
    "noakhali":           (22.8696, 91.0996),
    "lakshmipur":         (22.9425, 90.8418),
    "chandpur":           (23.2333, 90.6500),
    "brahmanbaria":       (23.9599, 91.1117),
    "bandarban":          (22.1953, 92.2184),
    "rangamati":          (22.6452, 92.1717),
    "khagrachari":        (23.1193, 91.9847),

    # Sylhet Division
    "habiganj":           (24.3745, 91.4152),
    "moulvibazar":        (24.4829, 91.7773),
    "moulvibazar":        (24.4829, 91.7773),
    "sunamganj":          (25.0658, 91.3950),

    # Mymensingh Division   
    "netrokona":          (24.8703, 90.7279),
    "jamalpur":           (24.9378, 89.9378),
    "sherpur":            (25.0194, 90.0159),

    # Rajshahi Division
    "bogra":              (24.8465, 89.3720),
    "sirajganj":          (24.4500, 89.7000),
    "pabna":              (24.0064, 89.2372),
    "natore":             (24.4200, 88.9800),
    "naogaon":            (24.8131, 88.9311),
    "joypurhat":          (25.1000, 89.0167),
    "chapai nawabganj":   (24.5957, 88.2736),
    "chapainawabganj":    (24.5957, 88.2736),

    # Khulna Division
    "jessore":            (23.1667, 89.2167),
    "jashore":            (23.1667, 89.2167),
    "satkhira":           (22.7185, 89.0705),
    "bagerhat":           (22.6602, 89.7854),
    "narail":             (23.1722, 89.5122),
    "magura":             (23.4878, 89.4192),
    "jhenaidah":          (23.5449, 89.1541),
    "kushtia":            (23.9014, 89.1214),
    "chuadanga":          (23.6401, 88.8418),
    "meherpur":           (23.7622, 88.6318),

    # Barisal Division
    "pirojpur":           (22.5789, 89.9751),
    "jhalokati":          (22.6333, 90.2000),
    "bhola":              (22.6861, 90.6480),
    "patuakhali":         (22.3596, 90.3298),
    "barguna":            (22.1500, 90.1167),

    # Rangpur Division
    "dinajpur":           (25.6279, 88.6337),
    "gaibandha":          (25.3288, 89.5282),
    "kurigram":           (25.8054, 89.6369),
    "lalmonirhat":        (25.9923, 89.2847),
    "nilphamari":         (25.9319, 88.8560),
    "thakurgaon":         (26.0318, 88.4616),
    "panchagarh":         (26.3411, 88.5542),

    # International Cities
    "london":             (51.5074, -0.1278),
    "new york":           (40.7128, -74.0060),
    "paris":              (48.8566,  2.3522),
    "tokyo":              (35.6762, 139.6503),
    "dubai":              (25.2048,  55.2708),
    "delhi":              (28.6139,  77.2090),
    "new delhi":          (28.6139,  77.2090),
    "mumbai":             (19.0760,  72.8777),
    "kolkata":            (22.5726,  88.3639),
    "singapore":          ( 1.3521, 103.8198),
    "bangkok":            (13.7563, 100.5018),
    "kuala lumpur":       ( 3.1390, 101.6869),
    "beijing":            (39.9042, 116.4074),
    "sydney":             (-33.8688, 151.2093),
    "toronto":            (43.6532,  -79.3832),
    "moscow":             (55.7558,  37.6173),
    "cairo":              (30.0444,  31.2357),
    "istanbul":           (41.0082,  28.9784),
    "riyadh":             (24.7136,  46.6753),
    "jeddah":             (21.5433,  39.1728),
    "karachi":            (24.8607,  67.0011),
    "lahore":             (31.5204,  74.3587),
    "islamabad":          (33.7294,  73.0931),
    "colombo":            ( 6.9271,  79.8612),
    "kathmandu":          (27.7172,  85.3240),
    "kabul":              (34.5553,  69.2075),
    "tehran":             (35.6892,  51.3890),
    "beijing":            (39.9042, 116.4074),
    "shanghai":           (31.2304, 121.4737),
    "hong kong":          (22.3193, 114.1694),
    "seoul":              (37.5665, 126.9780),
    "jakarta":            (-6.2088, 106.8456),
    "manila":             (14.5995, 120.9842),
    "rome":               (41.9028,  12.4964),
    "berlin":             (52.5200,  13.4050),
    "madrid":             (40.4168,  -3.7038),
    "amsterdam":          (52.3676,   4.9041),
    "los angeles":        (34.0522, -118.2437),
    "chicago":            (41.8781,  -87.6298),
    "washington":         (38.9072,  -77.0369),
    "washington dc":      (38.9072,  -77.0369),
    "doha":               (25.2854,  51.5310),
    "abu dhabi":          (24.4539,  54.3773),
    "nairobi":            (-1.2921,  36.8219),
    "johannesburg":       (-26.2041,  28.0473),
}

def nominatim_geocode(city_name):
    """Call Nominatim directly with browser-like headers."""
    try:
        resp = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": city_name, "format": "json", "limit": 1},
            headers={
                "User-Agent": "CityDistanceApp/2.0 (educational project)",
                "Accept-Language": "en"
            },
            timeout=10
        )
        data = resp.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception as e:
        print(f"Nominatim error: {e}")
    return None, None


def get_coords(city_name):
    """Tries local dict first, then Nominatim API."""
    key = city_name.lower().strip()

    # 1. Exact match in dictionary
    if key in CITY_COORDS:
        lat, lon = CITY_COORDS[key]
        return lat, lon

    # 2. Partial match (e.g. "cox bazar" matches "cox's bazar")
    for dict_key, coords in CITY_COORDS.items():
        if key in dict_key or dict_key in key:
            return coords

    # 3. Nominatim API fallback
    lat, lon = nominatim_geocode(city_name)
    if lat is not None:
        return lat, lon

    return None, None


# Debounce vars

debounce_timer = None
DEBOUNCE_DELAY = 0.9


def get_distance():
    city1 = city1_entry.get().strip()
    city2 = city2_entry.get().strip()

    if not city1 or not city2:
        root.after(0, lambda: result_label.config(text="Enter both cities above", fg="orange"))
        root.after(0, lambda: details_label.config(text=""))
        root.after(0, lambda: status_label.config(text=""))
        return

    root.after(0, lambda: status_label.config(text="Calculating...", fg="cyan"))
    root.after(0, lambda: result_label.config(text="Looking up cities...", fg="#aaaaaa"))

    coord1 = get_coords(city1)
    coord2 = get_coords(city2)

    if coord1 == (None, None):
        root.after(0, lambda: result_label.config(
            text=f"City not found: {city1.title()}", fg="red"))
        root.after(0, lambda: status_label.config(
            text="Try full name or check spelling", fg="orange"))
        return

    if coord2 == (None, None):
        root.after(0, lambda: result_label.config(
            text=f"City not found: {city2.title()}", fg="red"))
        root.after(0, lambda: status_label.config(
            text="Try full name or check spelling", fg="orange"))
        return

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dist_km = geodesic((lat1, lon1), (lat2, lon2)).km
    dist_mi = dist_km * 0.621371

    result_text = (
        f"{city1.title()}  ➜  {city2.title()}\n"
        f"{dist_km:.2f} KM   |   {dist_mi:.2f} Miles"
    )
    details_text = (
        f"📍 {city1.title()}: {lat1:.5f}°,  {lon1:.5f}°\n"
        f"📍 {city2.title()}: {lat2:.5f}°,  {lon2:.5f}°"
    )

    root.after(0, lambda: result_label.config(text=result_text, fg="#00ff99"))
    root.after(0, lambda: details_label.config(text=details_text, fg="#cccccc"))
    root.after(0, lambda: status_label.config(text="✅ Calculated successfully", fg="#00ff99"))


def threaded_distance(event=None):
    global debounce_timer
    if debounce_timer is not None:
        root.after_cancel(debounce_timer)
    debounce_timer = root.after(
        int(DEBOUNCE_DELAY * 1000),
        lambda: threading.Thread(target=get_distance, daemon=True).start()
    )

def button_calculate():
    threading.Thread(target=get_distance, daemon=True).start()


# UI

title = tk.Label(root, text="Find Distance Between Cities",
                 font=("Arial", 22, "bold"), bg="#121212", fg="white")
title.pack(pady=15)

city1_label = tk.Label(root, text="Enter First City",
                       font=("Arial", 13), bg="#121212", fg="#aaaaaa")
city1_label.pack()

city1_entry = tk.Entry(root, font=("Arial", 16), width=30,
                       relief="flat", bg="#1e1e1e", fg="white", insertbackground="white")
city1_entry.pack(pady=8, ipady=5)

city2_label = tk.Label(root, text="Enter Second City",
                       font=("Arial", 13), bg="#121212", fg="#aaaaaa")
city2_label.pack()

city2_entry = tk.Entry(root, font=("Arial", 16), width=30,
                       relief="flat", bg="#1e1e1e", fg="white", insertbackground="white")
city2_entry.pack(pady=8, ipady=5)

city1_entry.bind("<KeyRelease>", threaded_distance)
city2_entry.bind("<KeyRelease>", threaded_distance)

calculate_btn = tk.Button(root, text="Calculate Distance",
                          font=("Arial", 14, "bold"), bg="#00aaff", fg="white",
                          padx=15, pady=8, relief="flat", cursor="hand2",
                          command=button_calculate)
calculate_btn.pack(pady=15)

result_label = tk.Label(root, text="Distance will appear here",
                        font=("Arial", 18, "bold"), bg="#121212", fg="yellow",
                        wraplength=520, justify="center")
result_label.pack(pady=8)

details_label = tk.Label(root, text="", font=("Arial", 11),
                         bg="#121212", fg="#cccccc", justify="left")
details_label.pack()

status_label = tk.Label(root, text="", font=("Arial", 11, "italic"),
                        bg="#121212", fg="cyan")
status_label.pack(pady=8)

root.mainloop()