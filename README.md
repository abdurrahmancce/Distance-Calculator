# 🌍 Distance Calculator Between Two Cities

A modern and fully optimized **Distance Calculator Application** built with **Python Tkinter**.
This application calculates the accurate geographic distance between two cities using latitude and longitude coordinates with support for:

* ✅ 64 Bangladesh districts
* ✅ International cities
* ✅ Real-time distance calculation
* ✅ Live typing detection
* ✅ Network fallback using OpenStreetMap API
* ✅ Beautiful dark-mode UI
* ✅ Error handling and rate-limit protection

---

# 📸 Preview

A professional desktop GUI application that instantly calculates the straight-line distance between two cities in:

* Kilometers (KM)
* Miles

---

# ✨ Features

## 🌎 Accurate Distance Calculation

Uses the `geodesic()` method from **Geopy** for highly accurate Earth-distance calculations.

---

## 🇧🇩 64 Bangladesh Districts Included

Preloaded coordinates for all major Bangladesh cities and districts.

Examples:

* Dhaka
* Chittagong
* Sylhet
* Rajshahi
* Cox's Bazar
* Khulna
* Rangpur
* Barisal

---

## 🌐 International City Support

Supports worldwide cities using OpenStreetMap Nominatim API.

Examples:

* London
* Tokyo
* Paris
* Dubai
* New York
* Singapore
* Sydney

---

## ⚡ Real-Time Update

Distance updates automatically while typing.

---

## 🧠 Smart City Detection

Features:

* Exact city matching
* Partial city matching
* API fallback system
* Typo-friendly search

---

## 🚀 Network & Error Fixes

This version fixes:

* ❌ City not found errors
* ❌ API timeout problems
* ❌ Nominatim rate limiting
* ❌ App freezing issues

---

## 🖥️ Modern GUI

Built with:

* Dark mode theme
* Smooth interface
* Responsive layout
* Stylish buttons and labels

---

# 🛠️ Technologies Used

* Python
* Tkinter
* Geopy
* Requests
* Threading
* OpenStreetMap API

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/distance-calculator.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd distance-calculator
```

---

## 3️⃣ Install Dependencies

```bash
pip install geopy requests
```

---

# ▶️ Run The Application

```bash
python main.py
```

---

# 📂 Project Structure

```bash
distance-calculator/
│
├── main.py
├── README.md
```

---

# 🧮 How It Works

1. User enters two city names
2. App searches local city database
3. If not found:

   * Searches OpenStreetMap API
4. Coordinates are collected
5. Distance is calculated using:

```python
geodesic((lat1, lon1), (lat2, lon2)).km
```

6. Result is displayed instantly

---

# 📍 Example

## Input

```bash
City 1: Dhaka
City 2: Sylhet
```

## Output

```bash
199.45 KM
123.93 Miles
```

---

# 🔥 Advanced Features

## ✅ Debounce System

Prevents excessive API requests while typing.

---

## ✅ Multi-threading

Keeps GUI smooth and responsive.

---

## ✅ Offline Coordinate Support

Many cities work even without internet.

---

# 📈 Future Improvements

* 🗺️ Google Maps integration
* 📍 Route distance support
* 🚗 Driving distance calculation
* 🌍 Interactive map view
* 📌 GPS location detection

---

# 👨‍💻 Author

## Abdur Rahman Akash

<a href="https://github.com/abdurrahmancce">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</a>

<a href="https://www.linkedin.com/in/abdur-rahman-akash26/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>

<a href="mailto:akash.abdur.2002@gmail.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>

<a href="https://abdurrahmancce.github.io/Personal-Portfolio/">
  <img src="https://img.shields.io/badge/Portfolio-111827?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portfolio" />
</a>

---

# ⭐ Support

If you like this project:

* ⭐ Star this repository
* 🍴 Fork the project
* 🛠️ Contribute improvements

---

# 📜 License

This project is open-source and available under the MIT License.

