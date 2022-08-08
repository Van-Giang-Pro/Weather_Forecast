import requests

url = "https://api.openweathermap.org/data/2.5/forecast?q=Ho%20Chi%20Minh&appid=be63187149284bb1bae3e00e08f31774&units=metric"
r = requests.get(url)
print(r)
print(r.json())


class Weather:

	def __init__(self, apikey, city, lat, lon):
		url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
		r = requests.get(url)

	def next_12h(self):
		pass

	def next_12h_simplified(self):
		pass
