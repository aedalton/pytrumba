import requests
import datetime

# multipart csv parser aaron and hugh
class TrumbaParams(object):
    __startdate = ""
    __enddate = ""
    __months = ""
    __weeks = ""
    __previousweeks = ""
    __html = ""
    __customnotes = ""

   # def __init__(self, *args, **kwargs):
   #     """ """

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
        return self.__startdate

    @start_date.setter
    def start_date(self, date_value):
        """ Parameter to filter on start date of events.
        If not specified, uses the current date."""
        self.__startdate = "startdate={}".format(self.parse_date(date_value))

    @property
    def end_date(self):
        return self.__enddate

    @end_date.setter
    def end_date(self, date_value):
        """end date parameter; uses the same date format as for startdate"""
        self.__enddate = "enddate={}".format(self.parse_date(date_value))

    @property
    def query_string(self):
        query_base = "?"
        if self.__start_date != "":
            query_base += start_date

        return param_string

    
class TrumbaConfig(object):
    base_url = "http://www.trumba.com/calendars/gazette.json"



class TrumbaClient(object):
    def __init__(self):
        self.config = TrumbaConfig()
        self.params = TrumbaParams()

    #@property
    #def params(self):
    #    return self.__params.params

    def get(self):
        response = requests.get(self.config.base_url)
        import pdb; pdb.set_trace()
        return response

tc = TrumbaClient()
        
    
    
    

