# actransit_example.py
# Python_DS_Suite
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-11 14:48:11
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-11 23:22:51


__author__ = 'sidmishraw'

__PERSONAL_API_KEY__ = '7A94EF436CDBB9F1FB8624E0632CD54B'

# The base URL for the AC Transit APIs
__BASE_URL__ = 'https://api.actransit.org/transit'


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


# STOPS
# JSON object example - 
# {
#     "StopId": 58123,
#     "Name": "3rd St:Santa Clara Av",
#     "Latitude": 37.7732681,
#     "Longitude": -122.2882275,
#     "ScheduledTime": null
#   }
class ACTransitStop(object):
  'This is the implementation of the object model used by ACTransit for their \
  Stops JSON object.'

  def __init__(self, json_obj):
    '''Takes the JSON obj (decoded to python dict) and extracts the stopId, \
    name, latitude, longitude and \
    scheduled_time as the input\
    arguments to make this object.'''
    self.__json__ = json_obj
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
    'repr() calls this method.'
    return 'ACTransitStop({})'.format(repr(self.__json__))


# Predictions
# JSON example -
# {
#     "StopId": 56707,
#     "TripId": 5155418,
#     "VehicleId": 5021,
#     "RouteName": "19",
#     "PredictedDelayInSeconds": 540,
#     "PredictedDeparture": "2017-01-11T17:31:00",
#     "PredictionDateTime": "2017-01-11T17:10:41"
#   }
class ACTransitPrediction(object):
  'Wrapper class for the AC Transit\'s route prediction'

  def __init__(self, json_obj):
    'Takes the json_object representation(python dict) as the input and\
    initializes the prediction object.'
    self.__json__ = json_obj
    self.__stopId = json_obj['StopId']
    self.__tripId = json_obj['5155418']
    self.__vehicleId = json_obj['VehicleId']
    self.__route_name = json_obj['RouteName']
    self.__predicted_delay_in_secs = json_obj['PredictedDelayInSeconds']
    self.__predicted_departure = json_obj['PredictedDeparture']
    self.__predicted_date_time = json_obj['PredictionDateTime']

  @property
  def stopId(self):
    'The stopId as per AC Transit system.'
    return self.__stopId

  @property
  def tripId(self):
    'The tripId of the prediction as per the AC Transit system.'
    return self.__tripId

  @property
  def vehicleId(self):
    'The vehicleId of the prediction as per the AC Transit system.'
    return self.__vehicleId

  @property
  def route_name(self):
    'The route name of the prediction as per the AC Transit system.'
    return self.__route_name

  @property
  def predicted_delay_in_seconds(self):
    'The predicted delay in seconds as per the AC Transit system.'
    return self.__predicted_delay_in_secs

  @property
  def predicted_departure(self):
    'The predicted departure as per the AC Transit system.'
    return self.__predicted_departure

  @property
  def predicted_date_time(self):
    'The predicted data and time as per AC Transit system.'
    return self.__predicted_date_time

  def __repr__(self):
    'called by the repr()'
    return 'ACTransitPrediction({})'.format(repr(self.__json__))



# API wrappers for AC Transit

# GET stops
# Retrieve all of AC Transit's currently active stops.
def get_stops(user_api_key):
  'Gets all currently activ stops of the ACTransit system.'
  url = '%s/stops/?token=%s' % (__BASE_URL__, user_api_key)
  json_obj = None
  json_decoder = JSONDecoder()
  with urlopen(url) as req:
    json_obj = str(req.read(), encoding = 'utf-8')
  json_obj = json_decoder.decode(json_obj)
  ac_transit_stops = []
  for obj in json_obj:
    ac_transit_stops.append(ACTransitStop(obj))
  return ac_transit_stops

# GET stops/{latitude}/{longitude}/{distance}/{routeName}
# Retrieve all active stops within a certain radius (in feet) 
# of the given point. The default search radius is 500 feet.
def get_active_stops(user_api_key, latitude, longitude, search_radius = 500):
  'Retrieve all active stops within a certain radius (in feet) \
  of the given point. The default search radius is 500 feet.'
  pass

# GET stops/{latitude}/{longitude}?distance={distance}&routeName={routeName}
# Retrieve all active stops within a certain radius (in feet) 
# of the given point. The default search radius is 500 feet.
def get_active_stops_type2(user_api_key, latitude, longitude, search_radius = 500):
  'Retrieve all active stops within a certain radius (in feet) \
  of the given point. The default search radius is 500 feet.'
  pass

# GET stops/{stopId}/predictions  
# Retrieve vehicle predictions for a particular stop.
def get_predictions(user_api_key, stopId):
  'Retrieve vehicle predictions for a particular stop.'
  pass



def main():
  'main function does nothing since this is going to be a library module.\
  This cannot be run standalone as the main module. If run as main module, \
  this script does nothing.'
  # because this is going to be a library module
  # the main function should do nothing if this module is executed as
  # the main module.
  pass


if __name__ == '__main__':
  main()
  





