# 🗺️ QGIS Automation Scripts

Welcome to my collection of **Python scripts for QGIS**.  
These scripts automate common GIS workflows such as adding jurisdiction fields, joining shapefiles with Excel tables, validating unmatched records, and exporting data to GeoJSON.  

They are designed for **election data mapping, governance analysis, and telecom/GIS integration**, but can be adapted for many other use cases.

---

## 📂 Scripts Included

### 1. `add_juris_fields_flexible.py`
- Adds standard jurisdiction fields:
  - `JurisCat, State, Juristype, JurisTypeName, Jurislabel, JurisTypeID, Country`
- Generates a clean, lowercase `ShapeID` (alphanumeric only).
- Useful for creating **unique identifiers** across datasets.

---

### 2. `join_shapefile_excel_shapeid.py`
- Joins shapefile polygons with an Excel table of elected officials.
- Uses `ShapeID` as the common key field.
- Supports **1:M joins** (multiple officials linked to the same territory).

---

### 3. `find_unmatched.py`
- Identifies **unmatched records**:
  - Officials without polygons (`ShapeID` not found in shapefile).
  - Polygons without officials assigned.
- Saves results as separate shapefiles for validation.

---

### 4. `export_geojson.py`
- Exports the active QGIS layer to **GeoJSON format**.
- Useful for **web applications, dashboards, or data sharing**.

---

## 🛠 Example Workflow

1. Add and populate jurisdiction fields → `add_juris_fields_flexible.py`  
2. Join shapefile with Excel data → `join_shapefile_excel_shapeid.py`  
3. Validate integrity (find missing matches) → `find_unmatched.py`  
4. Export processed layer to GeoJSON → `export_geojson.py`  

---

## 📌 Requirements
- **QGIS 3.x** or higher installed.  
- Python environment bundled with QGIS.  
- Excel files must include a `ShapeID` column.  

---

## 👩‍💻 Author
**Marsela Rrokaj**  
🌍 GIS & Remote Sensing Specialist | Data Analyst  
📫 [LinkedIn](https://linkedin.com/in/marselarrokaj) | ✉️ marselarrokaj02@gmail.com  

---

✨ *Always learning, always mapping the world better.*
