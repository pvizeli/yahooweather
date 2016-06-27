"""This is a Python module that provides an interface to the Yahoo! Weather

    more details from https://github.com/pvizeli/yahooweather
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
    def __init__(self, woeid, unit=UNIT_C):
        """Init Object"""
        self._woeid = woeid
        self._unit = unit
        self._data = None

    def updateWeather(self):
        """Fetch weather data from Yahoo! True if success"""
        yql = _YAHOO_YQL.format(self._woeid, self._unit)
        url = _YAHOO_BASE_URL.format(urlencode({'q': yql}))

        # send request
        _LOGGER.debug("Send request to url: %s", url)
        try:
            request = urlopen(url)
            rawData = request.read()

            # parse jason
            data = json.loads(rawData.decode("utf-8"))

            self._data = data["query"]["results"]
            return True
        except urllib.error.HTTPError:
            _LOGGER.critical("Can't fetch data from Yahoo!")
            self._data = None

        return False

    @property
    def RawData(self):
        """Raw Data"""
        return self._data

    @property
    def Forecast(self):
        """Forecast data 0-5 Days"""
        if "forecast" in self._data:
            return self._data["forecast"]
        return {}

    @property
    def Now(self):
        """Current weather data"""
        if "condition" in self._data:
            return self._data["condition"]
        return {}
