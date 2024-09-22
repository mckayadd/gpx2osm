import argparse
import folium
from folium.features import DivIcon
from selenium import webdriver
import os
import time

def parse_gpx(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx_data = gpx_file.read()

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

def create_osm_overlay(coordinates):
    if len(coordinates) == 0:
        print("No coordinates found in the GPX file.")
        return None

    center_lat = sum(coord[0] for coord in coordinates) / len(coordinates)
    center_lon = sum(coord[1] for coord in coordinates) / len(coordinates)

    map_osm = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    route_line = folium.PolyLine(locations=coordinates, color='blue')
    route_line.add_to(map_osm)

    latitudes = [coord[0] for coord in coordinates]
    longitudes = [coord[1] for coord in coordinates]
    min_lat, max_lat = min(latitudes), max(latitudes)
    min_lon, max_lon = min(longitudes), max(longitudes)
    map_osm.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

    return map_osm

def save_as_png(map_osm, png_file):
    temp_html = "temp_map.html"
    map_osm.save(temp_html)

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--window-size=1920x1080")

    browser = webdriver.Firefox(options=firefox_options)
    browser.get("file://" + os.path.abspath(temp_html))

    time.sleep(1)
    browser.save_screenshot(png_file)
    browser.quit()

    os.remove(temp_html)

def main():
    parser = argparse.ArgumentParser(description='Convert GPS coordinates from GPX file to a PNG map.')
    parser.add_argument('--input', type=str, help='Input GPX file containing GPS coordinates.', required=True)
    parser.add_argument('--output', type=str, help='Output PNG file for the map screenshot.', required=True)

    args = parser.parse_args()
    coordinates = parse_gpx(args.input)
    map_osm = create_osm_overlay(coordinates)
    save_as_png(map_osm, args.output)

if __name__ == '__main__':
    main()
