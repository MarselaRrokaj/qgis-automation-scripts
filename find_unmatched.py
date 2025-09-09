# ===========================================
# Script: find_unmatched.py
# Author: Marsela Rrokaj
# Description: Identify unmatched elected officials and polygons using ShapeID
# ===========================================

from qgis.core import QgsVectorLayer
import processing

# Paths (update to your files)
shapefile_path = "path/to/shapefile.shp"
excel_path = "path/to/elected_officials.xlsx"
output_unmatched_officials = "unmatched_officials.shp"
output_unmatched_polygons = "unmatched_polygons.shp"

# Load shapefile
shapefile = QgsVectorLayer(shapefile_path, "territories", "ogr")

# Load Excel
excel_uri = f"Excel:?file={excel_path}&sheet=Sheet1"
excel_table = QgsVectorLayer(excel_uri, "officials", "ogr")

# 1) Officials without polygon
processing.run("qgis:joinattributestable", {
    "INPUT": excel_table,
    "FIELD": "ShapeID",
    "INPUT_2": shapefile,
    "FIELD_2": "ShapeID",
    "METHOD": 0,  # keep all records from first layer
    "DISCARD_NONMATCHING": False,
    "OUTPUT": output_unmatched_officials
})

print(f"✅ Officials without polygon saved to: {output_unmatched_officials}")

# 2) Polygons without officials
processing.run("qgis:joinattributestable", {
    "INPUT": shapefile,
    "FIELD": "ShapeID",
    "INPUT_2": excel_table,
    "FIELD_2": "ShapeID",
    "METHOD": 0,  # keep all polygons
    "DISCARD_NONMATCHING": False,
    "OUTPUT": output_unmatched_polygons
})

print(f"✅ Polygons without officials saved to: {output_unmatched_polygons}")
