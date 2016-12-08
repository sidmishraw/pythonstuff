# bo.py
# Has the business objects for the Account Management System
__author__ = 'sidmishraw'

from ams.constants.constants import AccountType
from ams.utils.utils import Money
from ams.utils.utils import Time

# Classes for accounts

class Account(object):
  """Account class

  """

  # automatic ID generator
  autoID = 0

  def __init__(self, name, account_type, balance=None, isReversed=False):
    """
      inits the account object not a constructor, but initializer
      self - object has already been constructed
      name - string - name of the account
      isReversed - boolean - if the account is reversed
      balance - Money - current balance of the account
      account_type - AccountType - Account type ASSET, etc
    """

    # correct way of accessing the static/class variable
    Account.autoID += 1

    self.__id = str(Account.autoID)
    self.__name = name
    self.__isReversed = isReversed
    # default balance is in U.S.D
    if balance == None:
      self.__balance = Money()
    else:
      self.__balance = balance
    self.__type = account_type

  def get_name(self):
    'fetches the account name'
    return self.__name

  def isReversed(self):
    'fetches the boolean isReversed for the Account'
    return self.__isReversed

  def get_balance(self):
    'fetches the balance of the account'
    return self.__balance

  def get_account_type(self):
    'fetches the account type'
    return self.__type



# Class for transaction
class Transaction(object):
  'Class for each transaction'

  autoID = 0

  def __init__(self, date, credited_account, debited_account, amount):
    'initializes Transaction \
     self - transaction object \
     date - Time class - custom made from utils \
     credited_account, debited_account - Account \
     amount - Money \
    '

    # correct way of accessing the static/class variable
    Transaction.autoID += 1

    self.__id = str(Transaction.autoID)
    self.__date = date
    self.__credited_account = credited_account
    self.__debited_account = debited_account
    self.__amount = amount


  def get_date(self):
    'fetches the date for the transaction'
    return self.__date

  def get_amount(self):
    'fetches the amount for the transaction'
    return self.__amount

  def get_credited_account(self):
    'fetches the credited account of the transaction'
    return self.__credited_account

  def get_debited_account(self):
    'fetches the debited account of the transaction'
    return self.__debited_account






