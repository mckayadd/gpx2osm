import folium

def create_osm_map(latitude, longitude):
    # Create a map centered at the given latitude and longitude
    map_osm = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker at the specified location
    folium.Marker([latitude, longitude]).add_to(map_osm)

    # Save the map as an HTML file
    map_osm.save("map.html")
    print("Map created successfully!")

# Example usage
latitude = 51.5074  # Example latitude (London)
longitude = -0.1278  # Example longitude (London)

create_osm_map(latitude, longitude)
