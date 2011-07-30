import datetime
import time

def epoch2datetime(epochsec):

    return datetime.datetime.fromtimestamp(epochsec)

def str2epoch(datestr, **kwargs): 

    return time.mktime(str2date(datestr), **kwargs)

def datetime2epoch(date):
    
    return time.mktime(date.timetuple())

def str2date(datestr, format_='%Y-%m-%d'):
    
    return datetime.datetime.strptime(datestr, format_).timetuple()


