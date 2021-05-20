import requests


api_url="http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
city=input("enter the city: ")
url = api_url + city

data = requests.get(url).json()
res= data["weather"][0]["main"]
print(res)