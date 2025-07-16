# 🗺️ University Location Viewer with HTML & JavaScript

This project is a simple web-based map tool that displays the location of universities using geographic data. It uses `where.html` and `where.js` to render university markers on an interactive map powered by the OpenLayers library.

## 📌 How It Works

- **`where.js`**: Contains location data for various universities (name, latitude, longitude).
- You can **add your own data** to this file by following the existing format.
- **`where.html`**: Loads the map in the browser and uses the data from `where.js` to show locations with clickable popups.

## 🌍 Features

- View the location of listed universities visually on a map
- Click on popups to see details like university name
- Easily customizable—just update `where.js` to add more universities

## 💡 Running the Project

You can run this in simple way:

### Directly in your browser
1. Navigate to the project folder
2. Double-click or right-click `where.html` and choose “Open in browser”
3. The map will load showing your configured locations

   This helps avoid any local file loading issues

## 📂 Other Files (Not Required to Run the Map Viewer)

- `geodump.py`, `geoload.py`, and `opengo.sqlite` appear to be related to an alternative geo data extraction process using Python and SQLite.
- These files may assist in dynamic location data generation, but are **not essential** for using or modifying `where.js` and `where.html`.

---

