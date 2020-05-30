import requests

from human import Human


class WeatherMan(Human):
    child = 0

    def __init__(self, name):
        super(WeatherMan, self).__init__(name)
        WeatherMan.child += 1

    def get_weather(self):
        response = requests.get("https://wttr.in", params={"format": 3})
        return f"{self}> За окном - {response.text}"

    def __str__(self):
        return "Синоптик"
