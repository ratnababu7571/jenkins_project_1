import requests
endpoint= "https://api.openweathermap.org/data/2.5/forecast?id=833&appid=61f8f465d80839ff07c6e7b60f51ae2e"
api_key = "61f8f465d80839ff07c6e7b60f51ae2e"
weather_params = {
    "latitude":47.159401,
    "logitide":34.330502,
    "appid":api_key,
    "cnt":4 
}
response = requests.get(endpoint,weather_params)
response_1=response.raise_for_status
data=response.json()
print(data)
 
