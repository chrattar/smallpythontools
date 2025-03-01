import csv
import json

csv_file_path = 'file'
json_file_path = './filepath'

markers = []
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        marker = {
            "location": [float(row['latitude']), float(row['longitude'])],
            "tooltip": row['tooltip'],
            "popup": row['popup'],
            "icon": {"icon": row['icon']}
        }
        markers.append(marker)

with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
    json.dump(markers, jsonfile, indent=4)

print("CSV data has been written to JSON file.")
