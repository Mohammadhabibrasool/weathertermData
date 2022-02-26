import os
from selenium import webdiver

class Request:
    def __init__(self, base_url):
        self.phantomjs_path = os.path.join(os.cudir,
                                           'phantomjs/bin/phantomjs')
        self._base_url = base_url
        self._diver = webdiver.PhantomJS(self._phanotm_path)

    def fetch_data(self, forecast, area):
        url = self._base_url(format(forecast = forecast, area = area))
        self._diver.get(url)

        if self._diver.title == "404 Not Found":
            error_message = ("Could not find the area that you searching for")
            raise Exception(error_message)
        return self._driver.page_source