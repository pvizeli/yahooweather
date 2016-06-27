import logging
from yahooweather import YahooWeather, UNIT_C

logging.basicConfig(level=logging.DEBUG)

yweather = YahooWeather(12891864, UNIT_C)
if yweather.updateWeather():
    print("%s", yweather.RawData)
else:
    print("Can't read data from yahoo!")
