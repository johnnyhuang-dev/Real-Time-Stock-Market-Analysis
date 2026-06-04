import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"TIME_SERIES_DAILY",
               "symbol":"MSFT",
               "outputsize":"compact",
               "datatype":"json"}

headers = {
	"x-rapidapi-key": "db137e4c80mshf1f73668cc6516dp130320jsnc9a95dff1130",
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())