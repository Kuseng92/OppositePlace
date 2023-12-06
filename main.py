from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geopy

def format_coordinates_for_google_maps(latitude, longitude):
    # Format coordinates as a Google Maps link
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def find_opposite_place(city_name):
    # Initialize a geocoder object (Nominatim)
    geolocator = Nominatim(user_agent="opposite_place_finder")

    try:
        # Get the coordinates of the input city
        location = geolocator.geocode(city_name)
        if location is None:
            return "City not found or coordinates unavailable."

        latitude = location.latitude
        longitude = location.longitude

        # Convert decimal degrees to degrees, minutes, seconds
        lat_deg = int(latitude)
        lat_min = int((latitude - lat_deg) * 60)
        lat_sec = int((latitude - lat_deg - lat_min / 60) * 3600)

        lon_deg = int(longitude)
        lon_min = int((longitude - lon_deg) * 60)
        lon_sec = int((longitude - lon_deg - lon_min / 60) * 3600)

        # Calculate the opposite coordinates
        opposite_latitude = -latitude
        opposite_longitude = (longitude + 180) % 360 - 180

        # Convert decimal degrees to degrees, minutes, seconds for the opposite coordinates
        opp_lat_deg = int(opposite_latitude)
        opp_lat_min = int((opposite_latitude - opp_lat_deg) * 60)
        opp_lat_sec = int((opposite_latitude - opp_lat_deg - opp_lat_min / 60) * 3600)

        opp_lon_deg = int(opposite_longitude)
        opp_lon_min = int((opposite_longitude - opp_lon_deg) * 60)
        opp_lon_sec = int((opposite_longitude - opp_lon_deg - opp_lon_min / 60) * 3600)

        # Format the coordinates as Google Maps links
        input_coordinates_link = format_coordinates_for_google_maps(latitude, longitude)
        opposite_coordinates_link = format_coordinates_for_google_maps(opposite_latitude, opposite_longitude)

        return f"Input City: {city_name}\nCoordinates: {lat_deg}° {lat_min}' {lat_sec}\" N, {lon_deg}° {lon_min}' {lon_sec}\" E\n"\
               f"Google Maps Link: {input_coordinates_link}\n\n"\
               f"Opposite Place Coordinates: {opp_lat_deg}° {opp_lat_min}' {opp_lat_sec}\" {'N' if opposite_latitude >= 0 else 'S'}, " \
               f"{opp_lon_deg}° {opp_lon_min}' {opp_lon_sec}\" {'E' if opposite_longitude >= 0 else 'W'}\n"\
               f"Google Maps Link (Opposite Place): {opposite_coordinates_link}"

    except GeocoderTimedOut:
        return "Geocoding request timed out. Please try again later."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    city_name = input("Enter the name of a city: ")
    result = find_opposite_place(city_name)
    print(result)
