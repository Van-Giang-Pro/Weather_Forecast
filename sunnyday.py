import requests, pprint


class Weather:

	def __init__(self, apikey, city, lat=None, lon=None):
		if city:
			url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
			r = requests.get(url)
			self.data = r.json()
		elif lat and lon:
			url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
			r = requests.get(url)
			self.data = r.json()
		else:
			raise TypeError("Provide Either A City Or Lat And Lon Arguments")

	def next_12h(self):
		return self.data["list"][:4]

	def next_12h_simplified(self):
		return self.data["list"][0]

weather = Weather(apikey="be63187149284bb1bae3e00e08f31774", city="Di An")
pprint.pprint(weather.next_12h_simplified())