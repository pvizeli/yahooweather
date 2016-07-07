yahooweather
============
Python modul for access to yahoo! weather

Example
-------
.. code:: python

    import logging
    from yahooweather import YahooWeather, UNIT_C

    logging.basicConfig(level=logging.WARNING)

    yweather = YahooWeather(91543049, UNIT_C)
    if yweather.updateWeather():
        print("RawData: %s" % str(yweather.RawData))
        print("Units: %s" % str(yweather.Units))
        print("Now: %s" % str(yweather.Now))
        print("Forecast: %s" % str(yweather.Forecast))
        print("Wind: %s" % str(yweather.Wind))
        print("Atmosphere: %s" % str(yweather.Atmosphere))
        print("Astronomy: %s" % str(yweather.Astronomy))

        data = yweather.Now
        print("Weather image from current: %s" %
              yweather.getWeatherImage(data["code"]))

        print("The woeid from Gstaad is: %s" % get_woeid(46.475661, 7.283469))
    else:
        print("Can't read data from yahoo!")

Rate Limits
-----------
Use of the Yahoo Weather API should not exceed reasonable request volume.
Access is limited to 2,000 signed calls per day.

Links
-----
- https://developer.yahoo.com/weather/
