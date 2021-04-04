#! python3
import requests

def getCitiesAroundYou(radiusinkm):
    coords = {
        'lat': "37.78087",
        'lng': "-122.49528"
    }
    header = {
    'Referer': "https://www.freemaptools.com/find-usa-cities-inside-radius.htm",
    'path': f"/ajax/find-usa-cities-inside-radius.php?lat={coords['lat']}&lng={coords['lng']}&sortaplha=0&radius={radiusinkm}"
    }
    res = requests.get(f"https://www.freemaptools.com/ajax/find-usa-cities-inside-radius.php?lat={coords['lat']}&lng={coords['lng']}&sortaplha=0&radius={radiusinkm}", headers=header)
    #res = requests.get(f"https://www.freemaptools.com/ajax/get-all-cities-inside.php?lat={coords['lat']}&lng={coords['long']}&sortaplha=0&radius={radiusinkm}", params=header)
    return res.json()

getCitiesAroundYou(30)