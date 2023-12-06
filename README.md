# **Opposite Place Finder**

This Python script, `main.py`, is a tool that helps you find the opposite place on the Earth's surface given the name of a city. It uses the Geopy library to geocode the input city, retrieve its coordinates, and calculate the coordinates of the opposite location.

## **How It Works**

The script performs the following steps:

- **Geocoding**: It initializes a geocoder object using Nominatim, a geocoding service. Then, it tries to obtain the coordinates (latitude and longitude) of the input city.

- **Coordinate Formatting**: After obtaining the coordinates, it converts them from decimal degrees to degrees, minutes, and seconds for both the input city and its opposite location.

- **Opposite Coordinates Calculation**: It calculates the coordinates of the opposite place by negating the latitude and finding the longitude's opposite value within the range of -180° to 180°.

- **Google Maps Links**: The script formats the input city's and opposite place's coordinates as Google Maps links, making it easy to visualize them on a map.

- **Output**: Finally, the script prints out the following information:

  - Input City Name
  - Coordinates of the Input City (in degrees, minutes, seconds)
  - Google Maps Link for the Input City
  - Coordinates of the Opposite Place (in degrees, minutes, seconds)
  - Google Maps Link for the Opposite Place

## **Usage**

- Run the script by executing it with Python: `main.py`
- Enter the name of a city when prompted.
- The script will provide information about the input city and its opposite place, along with Google Maps links for both locations.

## **Dependencies**

This script uses the following Python libraries:

- `geopy.geocoders` from Geopy for geocoding city names.
- `geopy.exc` from Geopy for handling geocoding exceptions.

## **Note**

- If the input city is not found or its coordinates are unavailable, the script will display an appropriate error message.
- In case of a geocoding request timeout, the script will inform you to try again later.
- Any other unexpected errors during the process will be displayed with an error message.

Enjoy using this tool to explore the opposite side of the Earth!
