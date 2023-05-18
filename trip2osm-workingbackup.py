import argparse
import folium

def parse_gpx(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx_data = gpx_file.read()

    # Extract coordinates from GPX data
    coordinates = []
    trkpt_start = gpx_data.find("<trkpt")
    while trkpt_start != -1:
        lat_start = gpx_data.find('lat="', trkpt_start) + 5
        lat_end = gpx_data.find('"', lat_start)
        lon_start = gpx_data.find('lon="', lat_end) + 5
        lon_end = gpx_data.find('"', lon_start)

        lat = float(gpx_data[lat_start:lat_end])
        lon = float(gpx_data[lon_start:lon_end])

        coordinates.append((lat, lon))

        trkpt_start = gpx_data.find("<trkpt", lon_end)

    return coordinates

def create_osm_overlay(coordinates, output_file):
    if len(coordinates) == 0:
        print("No coordinates found in the GPX file.")
        return

    # Calculate the center of the coordinates
    center_lat = sum(coord[0] for coord in coordinates) / len(coordinates)
    center_lon = sum(coord[1] for coord in coordinates) / len(coordinates)

    # Create a map centered at the calculated center
    map_osm = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add start and end points as markers with labels
    start_point = coordinates[0]
    end_point = coordinates[-1]

    folium.Marker(location=start_point, tooltip='Start', icon=folium.Icon(color='green', icon='play'),
                  popup=folium.Popup('Start', max_width=200)).add_to(map_osm)

    folium.Marker(location=end_point, tooltip='End', icon=folium.Icon(color='red', icon='stop'),
                  popup=folium.Popup('End', max_width=200)).add_to(map_osm)

    # Create a PolyLine to represent the route
    route_line = folium.PolyLine(locations=coordinates, color='blue')

    # Add the PolyLine to the map
    route_line.add_to(map_osm)

    # Save the map as an HTML file
    map_osm.save(output_file)

def main():
    # Create command line argument parser
    parser = argparse.ArgumentParser(description='Convert GPS coordinates from GPX file to OSM overlay.')
    parser.add_argument('--inputFile', type=str, help='Input GPX file containing GPS coordinates.')
    parser.add_argument('--outputFile', type=str, help='Output HTML file for the OSM overlay.')

    # Parse command line arguments
    args = parser.parse_args()

    # Parse GPX file and extract coordinates
    coordinates = parse_gpx(args.inputFile)

    # Create OSM overlay
    create_osm_overlay(coordinates, args.outputFile)

if __name__ == '__main__':
    main()
