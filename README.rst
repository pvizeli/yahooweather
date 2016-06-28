yahooweather
============
Python modul for access to yahoo! weather

Example
-------
.. code:: python

    import logging
    from yahooweather import YahooWeather, UNIT_C

    logging.basicConfig(level=logging.WARNING)

    yweather = YahooWeather(12891864, UNIT_C)
    if yweather.updateWeather():
        print("RawData: %s" % str(yweather.RawData))
        print("Now: %s" % str(yweather.Now))
        print("Forecast: %s" % str(yweather.Forecast))
        print("Wind: %s" % str(yweather.Wind))
        print("Atmosphere: %s" % str(yweather.Atmosphere))
        print("Astronomy: %s" % str(yweather.Astronomy))
    else:
        print("Can't read data from yahoo!")

Rate Limits
-----------
Use of the Yahoo Weather API should not exceed reasonable request volume. Access is limited to 2,000 signed calls per day.

Links
-----
- https://developer.yahoo.com/weather/
