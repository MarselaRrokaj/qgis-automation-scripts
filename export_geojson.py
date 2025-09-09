# ===========================================
# Script: export_geojson.py
# Author: Marsela Rrokaj
# Description: Exports the active QGIS layer to GeoJSON format
# ===========================================

from qgis.utils import iface
from qgis.core import QgsVectorFileWriter

# Get active layer
layer = iface.activeLayer()

if not layer:
    print("❌ No active layer selected!")
else:
    output_path = "path/to/output.geojson"  # change this path
    error = QgsVectorFileWriter.writeAsVectorFormat(
        layer,
        output_path,
        "UTF-8",
        driverName="GeoJSON"
    )

    if error[0] == QgsVectorFileWriter.NoError:
        print(f"✅ Layer exported successfully to {output_path}")
    else:
        print("❌ Export failed!")
