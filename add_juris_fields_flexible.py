# ===========================================
# Script: add_juris_fields_flexible.py
# Author: Marsela Rrokaj
# Description: Adds and populates jurisdiction fields in the active QGIS layer
# ===========================================

from qgis.utils import iface
from qgis.core import QgsField
from qgis.PyQt.QtCore import QVariant
import re

# Get active layer in QGIS
layer = iface.activeLayer()

if not layer:
    print("No active layer selected!")
else:
    print(f"Layer '{layer.name()}' loaded successfully.")

    # Start editing
    layer.startEditing()

    # Define fields
    new_fields = [
        QgsField("JurisCat", QVariant.String),
        QgsField("State", QVariant.String),
        QgsField("Juristype", QVariant.String),
        QgsField("JurisTypeName", QVariant.String),
        QgsField("Jurislabel", QVariant.String),
        QgsField("JurisTypeID", QVariant.String),
        QgsField("Country", QVariant.String),
        QgsField("ShapeID", QVariant.String)
    ]

    # Add missing fields
    provider = layer.dataProvider()
    existing_field_names = [field.name() for field in layer.fields()]

    for field in new_fields:
        if field.name() not in existing_field_names:
            provider.addAttributes([field])

    layer.updateFields()

    # 🔹 Values to populate (edit here for different projects)
    values = {
        "JurisCat": "Political",
        "State": "New Jersey",
        "Juristype": "st",
        "JurisTypeName": "New Jersey",
        "Jurislabel": "Senate District",
        "JurisTypeID": "District 21",
        "Country": "USA"   # always uppercase
    }

    # Function to clean text (lowercase + remove non-alphanumeric)
    def clean_text(text):
        text = text.lower().replace(" ", "")
        return re.sub(r'[^a-z0-9]', '', text)

    # Populate fields
    for feature in layer.getFeatures():
        for field_name, field_value in values.items():
            feature[field_name] = field_value

        # Build ShapeID (Country stays uppercase)
        shape_id = "_".join([
            clean_text(values["JurisCat"]),
            clean_text(values["State"]),
            clean_text(values["Juristype"]),
            clean_text(values["JurisTypeName"]),
            clean_text(values["Jurislabel"]),
            clean_text(values["JurisTypeID"]),
            values["Country"]  # stays uppercase
        ])

        feature["ShapeID"] = shape_id
        layer.updateFeature(feature)

    # Commit changes
    layer.commitChanges()
    print("✅ All fields added and populated successfully!")
