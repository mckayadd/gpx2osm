import argparse
import xml.etree.ElementTree as ET
import folium
from folium.features import DivIcon


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

    # folium.Marker(location=start_point, tooltip='Start', icon=folium.Icon(color='green', icon='play'),
    #               ).add_to(map_osm)

    # folium.Marker(location=end_point, tooltip='End', icon=folium.Icon(color='red', icon='stop'),
    #               ).add_to(map_osm)


    #------------------------------------------------------------------
        # Start point
    folium.Marker(
        location=coordinates[0], 
        popup=folium.Popup('<b>Start</b>', max_width=200), 
        icon=folium.Icon(color='green', icon='play')
    ).add_to(map_osm)

    folium.map.Marker(
        [coordinates[0][0], coordinates[0][1]],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            #html='<div style="font-size: 24pt; color : black">Start</div>',
        )
    ).add_to(map_osm)

    # End point
    folium.Marker(
        location=coordinates[-1], 
        popup=folium.Popup('<b>End</b>', max_width=200), 
        icon=folium.Icon(color='red', icon='stop')
    ).add_to(map_osm)

    folium.map.Marker(
        [coordinates[-1][0], coordinates[-1][1]],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            #html='<div style="font-size: 24pt; color : black">End</div>',
        )
    ).add_to(map_osm)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Roundabouts
    #------------------------------------------------------------------

    # RA1
    folium.Marker(
        location=[57.70974, 11.91848], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        [57.70974, 11.91848],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA1</div>',
        )
    ).add_to(map_osm)
    # !-!


    # RA2
    folium.Marker(
        location=[57.70210, 11.91155], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        [57.70210, 11.91155],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA2</div>',
        )
    ).add_to(map_osm)
    # !-!

    # RA3
    folium.Marker(
        location=[57.70655, 11.92205], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        [57.70655, 11.92205],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA3</div>',
        )
    ).add_to(map_osm)
    # !-!

    # RA4
    folium.Marker(
        location=[57.70998, 11.92721], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        [57.70998, 11.92721],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA4</div>',
        )
    ).add_to(map_osm)
    # !-!
    
    # RA5
    folium.Marker(
        location=[57.71007, 11.93112], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        location=[57.71007, 11.93112],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA5</div>',
        )
    ).add_to(map_osm)
    # !-!

    # RA6
    folium.Marker(
        location=[57.70771, 11.93477], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        [57.70771, 11.93477],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA6</div>',
        )
    ).add_to(map_osm)
    # !-!

    # RA7
    folium.Marker(
        location=[57.71113, 11.94337], 
        #popup=folium.Popup('<b>Start</b>', max_width=200), 
        #icon=folium.Icon(color='black', icon='map-marker')
    ).add_to(map_osm)

    folium.map.Marker(
        [57.71113, 11.94337],
        icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(0,0),
            html='<div style="font-size: 16pt; color : red; font-weight: bold;";>RA7</div>',
        )
    ).add_to(map_osm)
    # !-!

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



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
