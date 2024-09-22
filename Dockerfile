# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set up non-root user
RUN useradd -m user
USER user
WORKDIR /home/user

# Install the required Python libraries
RUN pip install --no-cache-dir folium selenium

# Install Firefox and Geckodriver
USER root
RUN apt-get update && apt-get install -y wget firefox-esr unzip \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.30.0-linux64.tar.gz \
    && rm geckodriver-v0.30.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && chown root:root /usr/local/bin/geckodriver

# Copy the script to the container
COPY gpx2osm.py /opt/gpx2osm.py

# Switch back to non-root user
USER user
