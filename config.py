# AIS Stream Configuration
# Configuration file for AIS stream monitoring parameters

# Ship MMSI filters - list of MMSI numbers to monitor
# Example: ["244528000", "123456789", "987654321"]
FILTERS_SHIP_MMSI_ID = ["244528000","268855"]

# Vessel Information
VESSEL_INFO = {
    'name': 'Regina Maris',
    'prefix': 'S/V',  # Sailing Vessel
    'mmsi': '244528000',
    'imo': '7025126',
    'call_sign': 'unknown',
    'flag_state': 'The Netherlands',
    'vessel_type': 'Three-masted topsail schooner (sailing vessel)',
    'gross_tonnage': '153 GT',
    'length': '48 m',
    'beam': '6.9 m',
    'draft': '2.9 m',
    'master': 'tbd',
    'owner': 'tbd'
}

# Logbook Settings
LOGBOOK_SETTINGS = {
    'title': 'NAUTISCHES LOGBUCH',
    'subtitle': 'Fahrtenbuch',
    'show_mmsi': True,
    'show_imo': True,
    'show_call_sign': False,
    'show_flag_state': True,
    'show_vessel_type': True,
    'show_master': False,
    'show_gross_tonnage': True,
    'show_dimensions': True
}

# Maximum monitoring duration in minutes
# How long to monitor the AIS stream before stopping
MAX_DURATION_MINUTES = 5

# Time threshold in hours for duplicate entry filtering
# Skip new entries if the latest entry is younger than this threshold
TIME_THRESHOLD_HOURS = 0.15

# Bounding boxes for geographical filtering
# Each bounding box is defined by two coordinates: [[lat1, lon1], [lat2, lon2]]
# Example: [[[34, 18], [42, 30]]] Aegean Sea

#"BoundingBoxes": [[[-90, -180], [90, 180]]], # Worldwide

# Approximate bounding box for the Aegean Sea
#BOUNDING_BOXES = [[[34, 18], [42, 30]]]

# North Atlantic Ocean ande carribean sea
BOUNDING_BOXES = [[[-7.22,-105.15], [61.77,14.77]]]
