# utils.py
# has the utility class definitions
# Includes Time and Money

# intra package imports are taken care of by the 
# Never run this as a script, since Python won't know
# root package, the imports will fail
# instead use example.py


from ams.exception.exception import NotSameCurrencyException

__author__ = 'sidmishraw'

# Custom Money class
class Money(object):
  'Money class custom made for AMS'
  # init for the money class
  # currency_symbol - symbol for the currency - defaults to $
  # amount - amount of money - defaults to 0.0
  # currency_full_name - 
  #   Complete name for the currency - defaults to United States Dollar
  def __init__(self, currency_symbol = '$'
    , amount = 0.0, currency_full_name = 'United States Dollar'):
    """
      initializes a Money object with the currency_symbol,
      amount and currency_full_name
    """

    # since the fields are private and associated with the instance 
    # they begin with __ to enable Python's automatic
    # name mangling
    self.__currency_symbol = currency_symbol
    self.__amount = amount
    self.__currency_full_name = currency_full_name


  # getters for private fields
  def get_currency_symbol(self):
    'gets the currency symbol'
    return self.__currency_symbol

  def get_amount(self):
    'gets the amount of money'
    return self.__amount

  def get_currency_full_name(self):
    'gets the full name of the currency for money'
    return self.__currency_full_name

  # comparators for Money, since it is a value class
  def __eq__(self,other):
    'checks for equality'
    if self.__currency_symbol == other.__currency_symbol \
      and self.__currency_full_name == other.__currency_full_name \
      and self.__amount == other.__amount:

      return True
    else:
      return False

  def __ne__(self,other):
    'checks not equals, delegates the check to __eq__()'
    return not (self == other)

  def __lt__(self,other):
    'checks less than if self < other, raises NotSameCurrencyException'
    if self.__currency_symbol != other.__currency_symbol \
      or self.__currency_full_name != other.__currency_full_name:
      raise NotSameCurrencyException('Currencies are not same, can\'t compare')
    elif self.__amount < other.__amount:
      return True
    else:
      return False

  def __le__(self,other):
    'checks less than or equals, i.e if self <= other \
    , raises NotSameCurrencyException'
    if self.__currency_symbol != other.__currency_symbol \
      or self.__currency_full_name != other.__currency_full_name:
      raise NotSameCurrencyException('Currencies are not same, can\'t compare')
    elif self.__amount <= other.__amount:
      return True
    else:
      return False

  def __gt__(self,other):
    'checks greater than if self < other, raises NotSameCurrencyException'
    if self.__currency_symbol != other.__currency_symbol \
      or self.__currency_full_name != other.__currency_full_name:
      raise NotSameCurrencyException('Currencies are not same, can\'t compare')
    elif self.__amount > other.__amount:
      return True
    else:
      return False

  def __ge__(self,other):
    'checks greater than or equals, i.e if self <= other \
    , raises NotSameCurrencyException'
    if self.__currency_symbol != other.__currency_symbol \
      or self.__currency_full_name != other.__currency_full_name:
      raise NotSameCurrencyException('Currencies are not same, can\'t compare')
    elif self.__amount >= other.__amount:
      return True
    else:
      return False

  def __repr__(self):
    'returns the string representation for Money'
    return self.__currency_symbol + " " + str(round(self.__amount,2))

  def __str__(self):
    'the toString() in Python, converts to string, string representation \
    of Money'
    return self.__currency_symbol + " " + str(round(self.__amount,2))


# importing datetime module to work with the string conversions into python
# datetime
from datetime import datetime

# Custom class for time
class Time(object):
  'Custom class for time for use in AMS'

  def __generate_time_stamp__(self):
    'private method to generate the timestamp for the instance'
    date_obj = datetime.strptime(str(self),"%m-%d-%Y")
    return int(date_obj.timestamp())


  def __init__(self, month, day, year):
    'initialize the Time object, customized for AMS'
    self.__month = str(month)
    self.__day = str(day)
    self.__year = str(year)
    self.__timestamp = Time.__generate_time_stamp__(self)

  def get_month(self):
    'fetches the month of the Time object'
    return self.__month

  def get_year(self):
    'fetches the year of the Time object'
    return self.__year

  def get_day(self):
    'fetches the day of the Time object'
    return self.__day

  # repr and str represenations of time
  def __str__(self):
    'string format for Time object'
    return self.__month.zfill(2) + "-" + self.__day.zfill(2) \
      + "-" + self.__year.zfill(4)

  def __repr__(self):
    'string representation for Time object'
    return self.__month.zfill(2) + "-" + self.__day.zfill(2) \
      + "-" + self.__year.zfill(4)

  # comparators for the Time
  def __eq__(self,other):
    'equality - if self == other'
    if self.__timestamp == other.__timestamp:
      return True
    else:
      return False

  def __ne__(self,other):
    'not equals - if self != other'
    return not __eq__(self,other)

  def __lt__(self,other):
    'less than - if self < other'
    if self.__timestamp < other.__timestamp:
      return True
    else:
      return False

  def ___le__(self,other):
    'less than or equals - if self <= other'
    if self.__timestamp <= other.__timestamp:
      return True
    else:
      return False

  def __gt__(self,other):
    'greater than - if self > other'
    if self.__timestamp > other.__timestamp:
      return True
    else:
      return False

  def __ge__(self,other):
    'greater than or equals to - if self >= other'
    if self.__timestamp >= other.__timestamp:
      return True
    else:
      return False

  # implementing the hash function to make Time class
  # hashable, so that it can be used as keys in the dicts
  def __hash__(self):
    'custom hash function, computes the hashes based on the timestamp'
    return hash(self.__timestamp)




    







