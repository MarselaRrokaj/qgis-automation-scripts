# QGIS Automation Script – Add and Populate Jurisdiction Fields

## 📌 Description
This repository contains a Python script for **QGIS** that automates the process of adding and populating jurisdiction-related fields into the attribute table of the **active layer**.  
It is designed for workflows involving **election mapping, governance data, and jurisdictional analysis**.

## 🔹 Features
- Automatically adds the following fields if they don’t exist:
  - `JurisCat`
  - `State`
  - `Juristype`
  - `JurisTypeName`
  - `Jurislabel`
  - `JurisTypeID`
  - `Country`
  - `ShapeID`
- Populates fields with predefined values (easy to edit inside the script).
- Generates a **ShapeID** by concatenating all values:
  - Converts everything to **lowercase + alphanumeric only** (no spaces or special characters).
  - Keeps `Country` in **uppercase**.
- Works on the **active layer** in QGIS (no need to reload shapefile).

## 🛠 Example Output
With the following values:
- JurisCat = Political  
- State = New Jersey  
- Juristype = st  
- JurisTypeName = New Jersey  
- Jurislabel = Senate District  
- JurisTypeID = District 21  
- Country = USA  

The generated `ShapeID` will be:
political_newjersey_st_newjersey_senatedistrict_district21_USA


## 🚀 Usage
1. Open QGIS and load your shapefile.  
2. Select the layer you want to edit (make it the **active layer**).  
3. Open the **Python Console** in QGIS.  
4. Copy and paste the script `add_juris_fields_flexible.py`.  
5. Run it – the new fields will be created and automatically populated.  

## 📌 Notes
- Update the `values = {...}` dictionary in the script for different states, districts, or projects.  
- The script ensures clean IDs for consistent data management.  

---

👩‍💻 **Author**: Marsela Rrokaj  

