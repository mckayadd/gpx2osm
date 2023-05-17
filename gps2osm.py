import csv
import argparse
import folium

def create_osm_overlay(coordinates, output_file):
    # Calculate the center of the coordinates
    center_lat = sum(coord[0] for coord in coordinates) / len(coordinates)
    center_lon = sum(coord[1] for coord in coordinates) / len(coordinates)

    # Create a map centered at the calculated center
    map_osm = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add a marker for each coordinate
    for coord in coordinates:
        folium.Marker(location=[coord[0], coord[1]]).add_to(map_osm)

    # Save the map as an HTML file
    map_osm.save(output_file)

def main():
    # Create command line argument parser
    parser = argparse.ArgumentParser(description='Convert GPS coordinates to OSM overlay.')
    parser.add_argument('--inputFile', type=str, help='Input CSV file containing GPS coordinates.')
    parser.add_argument('--outputFile', type=str, help='Output HTML file for the OSM overlay.')

    # Parse command line arguments
    args = parser.parse_args()

    # Read coordinates from CSV file
    coordinates = []
    with open(args.inputFile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            lat, lon = float(row[0]), float(row[1])
            coordinates.append((lat, lon))

    # Create OSM overlay
    create_osm_overlay(coordinates, args.outputFile)

if __name__ == '__main__':
    main()
