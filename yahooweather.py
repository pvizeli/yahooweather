"""This is a Python module that provides an interface to the Yahoo! Weather

more details from https://github.com/pvizeli/yahooweather
or API: https://developer.yahoo.com/weather/
"""
import json
import logging
import urllib.error
from urllib.parse import urlencode
from urllib.request import urlopen

_YAHOO_BASE_URL = "https://query.yahooapis.com/v1/public/yql?{0}&format=json"
_YQL_WEATHER = "SELECT * FROM weather.forecast WHERE woeid = '{0}' and u='{1}'"
_YQL_WOEID = "SELECT woeid FROM geo.places WHERE text = '({0},{1})'"

UNIT_C = 'c'
UNIT_F = 'f'

_LOGGER = logging.getLogger(__name__)


def _yql_query(yql):
    """Fetch data from Yahoo! Return a dict if successfull or None."""
    url = _YAHOO_BASE_URL.format(urlencode({'q': yql}))

    # send request
    _LOGGER.debug("Send request to url: %s", url)
    try:
        request = urlopen(url)
        rawData = request.read()

        # parse jason
        data = json.loads(rawData.decode("utf-8"))

        _LOGGER.debug("Query data from yahoo: %s", str(data))
        return data.get("query", {}).get("results", {})

    except (urllib.error.HTTPError, urllib.error.URLError):
        _LOGGER.info("Can't fetch data from Yahoo!")

    return None


def get_woeid(lat, lon):
    """Ask Yahoo! who is the woeid from GPS position."""
    yql = _YQL_WOEID.format(lat, lon)

    # send request
    tmpData = _yql_query(yql)

    if tmpData is None:
        _LOGGER.error("No woid is received!")
        return None

    # found woid?
    return tmpData.get("place", {}).get("woeid", None)


class YahooWeather(object):
    """Yahoo! API access."""

    def __init__(self, woeid, unit=UNIT_C):
        """Init Object."""
        self._woeid = woeid
        self._unit = unit
        self._data = {}

    def updateWeather(self):
        """Fetch weather data from Yahoo! True if success."""
        yql = _YQL_WEATHER.format(self._woeid, self._unit)

        # send request
        tmpData = _yql_query(yql)

        # data exists
        if tmpData is not None and "channel" in tmpData:
            self._data = tmpData["channel"]
            return True

        _LOGGER.error("Fetch no weather data Yahoo!")
        self._data = {}
        return False

    @property
    def RawData(self):
        """Raw Data."""
        return self._data

    @property
    def Units(self):
        """Return dict with units."""
        return self._data.get("units", {})

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

    def getWeatherImage(self, code):
        """Create a link to weather image from yahoo code."""
        return "https://l.yimg.com/a/i/us/we/52/{}.gif".format(code)
