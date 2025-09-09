# ===========================================
# Script: join_shapefile_excel_shapeid.py
# Author: Marsela Rrokaj
# Description: Joins shapefile polygons with elected officials data (Excel) using ShapeID
# ===========================================

from qgis.core import QgsVectorLayer
import processing

# Paths (update to your files)
shapefile_path = "path/to/shapefile.shp"
excel_path = "path/to/elected_officials.xlsx"
output_path = "joined_output.shp"

# Load shapefile
shapefile = QgsVectorLayer(shapefile_path, "territories", "ogr")
if not shapefile.isValid():
    print("❌ Shapefile failed to load!")

# Load Excel
excel_uri = f"Excel:?file={excel_path}&sheet=Sheet1"
excel_table = QgsVectorLayer(excel_uri, "officials", "ogr")
if not excel_table.isValid():
    print("❌ Excel table failed to load!")

# Join Attributes by Field Value (1:M join)
processing.run("qgis:joinattributestable", {
    "INPUT": shapefile,
    "FIELD": "ShapeID",
    "INPUT_2": excel_table,
    "FIELD_2": "ShapeID",
    "METHOD": 1,  # separate feature for each matching record
    "DISCARD_NONMATCHING": False,
    "OUTPUT": output_path
})

print(f"✅ Join completed! Output saved to: {output_path}")
