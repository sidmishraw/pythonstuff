# actransit_example.py
# Python_DS_Suite
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-11 14:48:11
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-11 17:08:29


__author__ = 'sidmishraw'
__PERSONAL_API_KEY__ = '7A94EF436CDBB9F1FB8624E0632CD54B'


# for processing JSON
from json import dumps
from json import loads
from json import JSONDecoder
from json import JSONEncoder

# for processing the requests(sending)
from urllib.request import urlopen
from urllib.request import Request

# for processing the response(receiving)
import urllib.response

# gonna use the webbrowser to ping me when theh bus is nearby
import webbrowser



class ACTransitStopsObject(object):
  'This is the implementation of the object model used by ACTransit for their \
  JSON object.'

  def __init__(self, json_obj):
    '''Takes the JSON obj (decoded to python dict) and extracts the stopId, \
    name, latitude, longitude and \
    scheduled_time as the input\
    arguments to make this object.'''
    self.__stopId = json_obj['StopId']
    self.__name = json_obj['Name']
    self.__latitude = json_obj['Latitude']
    self.__longitude = json_obj['Longitude']
    self.__scheduled_time = json_obj['ScheduledTime']

  @property
  def stopId(self):
    'The stopId as per AC Transit system.'
    return self.__stopId

  @property
  def name(self):
    'The name of the stop as per the AC Transit system.'
    return self.__name
  
  @property
  def latitude(self):
    'The latitude of the stop as per the AC Transit system.'
    return self.__latitude

  @property
  def longitude(self):
    'The longitude of the stop as per the AC Transit system.'
    return self.__longitude

  @property
  def scheduled_time(self):
    'The scheduled time for the bus as per the AC Transit system.'
    return self.__scheduled_time

  def __repr__(self):
    'The repr() value of this object, can be used as python command directly.\
    Of form (stopId, name, latitude, longitude, scheduled time)'
    return '(%s, %s, %s, %s, %s)' % (self.__stopId, self.__name,\
      self.__latitude, self.__longitude, self.__scheduled_time)




# API wrappers for AC Transit
def get_stops():
  'Gets all currently activ stops of the ACTransit system.'
  url = 'https://api.actransit.org/transit/stops/?token=%s' % __PERSONAL_API_KEY__
  json_obj = None
  json_decoder = JSONDecoder()
  with urlopen(url) as req:
    json_obj = str(req.read(), encoding = 'utf-8')
  json_obj = json_decoder.decode(json_obj)
  ac_transit_stops = []
  for obj in json_obj:
    ac_transit_stops.append(ACTransitStopsObject(obj))
  return ac_transit_stops




def main():
  'main function'
  get_stops()


if __name__ == '__main__':
  main()
  





