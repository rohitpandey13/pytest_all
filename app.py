import requests
def get_weather(city):
    #response = requests.get(f"https://api.weather.com/{city}")
    response = requests.get(f"https://wbypp.free.beeceptor.com")
    print(5/int(response.text))
    return response.json()