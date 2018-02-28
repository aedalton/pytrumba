import datetime
import json
import ntpath
import requests
import shutil


class TrumbaParams(object):
    __params = {}
    def __init__(self):
        self.__params["enddate"] = ""
        self.__params["startdate"] = ""
        self.__params["months"] = ""
        self.__params["weeks"] = ""
        self.__params["previousweeks"] = ""
        self.__params["html"] = ""
        self.__params["customnotes"] = ""

    def parse_date(self, date_value):
        """ Trumba accepted date format is
        yyyymmdd, for example, 20161205 for 5 Dec. 2016."""
        try:
            datetime.datetime.strptime(date_value, '%Y%m%d')
            return date_value
        except ValueError:  # could parse it for them...but
            raise ValueError("Incorrect data format, should be YYYYMMDD")

    @property
    def start_date(self):
        return self.__params["startdate"]

    @start_date.setter
    def start_date(self, date_value):
        """ Parameter to filter on start date of events.
        If not specified, uses the current date."""
        self.__params["startdate"] = self.parse_date(date_value)

    @property
    def end_date(self):
        return self.__params["enddate"]

    @end_date.setter
    def end_date(self, date_value):
        """end date parameter; uses the same date format as for startdate"""
        self.__params["enddate"] = self.parse_date(date_value)

    @property
    def query_string(self):
        return self.__params


class TrumbaConfig(object):
    base_url = "http://www.trumba.com/calendars/gazette.json"


class TrumbaClient(object):
    config = TrumbaConfig()
    params = TrumbaParams()

    def get(self):
        response = requests.get(self.config.base_url, params=self.params.query_string)
        print(response.url)
        return response

    def get_parsed(self):
        response = self.get()
        return json.loads(response.text)
