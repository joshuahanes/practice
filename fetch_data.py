import requests

url = "https://api.open-meteo.com/v1/forecast"

response=requests.get(url,
                      params={"latitude":37.55,
                      "longitude":-77.46,
                      "current":"temperature_2m"})
data=response.json()
print(data.keys())
print(data["current"])