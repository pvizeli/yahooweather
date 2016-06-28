"""This is a Python module that provides an interface to the Yahoo! Weather

more details from https://github.com/pvizeli/yahooweather
or API: https://developer.yahoo.com/weather/
"""
import json
import logging
from urllib.parse import urlencode
from urllib.request import urlopen

_YAHOO_BASE_URL = "https://query.yahooapis.com/v1/public/yql?{0}&format=json"
_YAHOO_YQL = "select * from weather.forecast where woeid = '{0}' and u='{1}'"

UNIT_C = 'c'
UNIT_F = 'f'

_LOGGER = logging.getLogger(__name__)


class YahooWeather(object):
    """Yahoo! API access."""
    def __init__(self, woeid, unit=UNIT_C):
        """Init Object."""
        self._woeid = woeid
        self._unit = unit
        self._data = {}

    def updateWeather(self):
        """Fetch weather data from Yahoo! True if success."""
        yql = _YAHOO_YQL.format(self._woeid, self._unit)
        url = _YAHOO_BASE_URL.format(urlencode({'q': yql}))

        # send request
        _LOGGER.debug("Send request to url: %s", url)
        try:
            request = urlopen(url)
            rawData = request.read()

            # parse jason
            data = json.loads(rawData.decode("utf-8"))

            _LOGGER.debug("Query data from yahoo: %s", str(data))
            tmpData = data.get("query", {}).get("results", {})

            # data exists
            if "channel" in tmpData:
                self._data = tmpData["channel"]
                return True
            else:
                _LOGGER.error("Fetch no weather data Yahoo!")
                self._data = {}
                return False

        except urllib.error.HTTPError:
            _LOGGER.critical("Can't fetch data from Yahoo!")

        return False

    @property
    def RawData(self):
        """Raw Data."""
        return self._data

    @property
    def Forecast(self):
        """Forecast data 0-5 Days."""
        return self._data.get("item", {}).get("forecast", None)

    @property
    def Now(self):
        """Current weather data."""
        return self._data.get("item", {}).get("condition", None)

    @property
    def Astronomy(self):
        """Astronomy weather data."""
        return self._data.get("astronomy", None)

    @property
    def Atmosphere(self):
        """Atmosphere weather data."""
        return self._data.get("atmosphere", None)

    @property
    def Wind(self):
        """Wind weather data."""
        return self._data.get("wind", None)
