import requests
def fetch_data(lat=37.55,lon=-77.46):
    """This function takes a lat long and returns temp and air qual"""

    url1 = "https://"
    url2 = "https://"


    response=requests.get(
        url1,
        params={
            "latitude":lat,
            "longitude":long,
            "current":"temperature_2m"

        })
    data=response.json()
    temperature=data["current"]["temperature_2m"]

    response=requests.get(
        url1,
        params={
            "latitude":lat,
            "longitude":long,
            "current":"temperature_2m"
    
        })
    data=response.json()
    temperature=data["current"]["temperature_2m"]