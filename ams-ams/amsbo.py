# This module contains all the Business Objects for this Account Management System application
# author - sidmishraw

__author__ = 'sidmishraw'


class Money(object):
  """
    This is the Money class. This is a value type class.
    Hence this is immutable.
  """
  # instantiates Money object
  # Money has currency and value
  def __init__(self,currency = '$',amount = 0.00, currencyFullName = "United States Dollar"):
    """
      This is the initiator for the Money class. It takes the currency symbol
      which is by default '$' for U.S.D and amount which is by default 0.00
      and creates a Money object.
    """
    self.__currency = currency
    self.__amount = amount
    self.__currencyFullName = currencyFullName

  def getcurrency(self):
    """
     Fetches the currency symbol of the Money object.
    """
    return self.__currency

  def getamount(self):
    """
     Fetches the amount value of the Money object.
    """
    return self.__amount

  def getcurrencyfullname(self):
    """
     Fetches the currency full name of the Money object.
    """
    return self.__currencyFullName

  def __str__(self):
    return " ".join((self.__currency,str(self.__amount),self.__currencyFullName))


if __name__ == '__main__':
  print('This module is meant only to be imported and not called directly.')
  exit(1)
