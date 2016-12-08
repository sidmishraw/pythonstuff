# service.py
# services for AMS
# singleton pattern followed in these class
'module having the services for AMS'

__author__ = 'sidmishraw'

from ams.dao.dao import AMSDao
from ams.bo.bo import Account
from ams.bo.bo import Transaction
from ams.utils.utils import Time
from ams.utils.utils import Money
import time


# Note - Do I need the services to be instance methods of a service class
# or just functions of my service module.

# Just for the sakes of it, I'm gonna make a singleton service class

class AMSService(object):
  'AMS service class'

  # The private inner class
  # The actual service class
  # The outer class is there to make the inner class singleton
  class __AMSService(object):
    'private inner class for AMS service class'

    def __init__(self):
      pass

    def create_account(self, account_name=None, account_type=None):
      'creates an account from the given account_name and account_type'
      dao = AMSDao()
      account = Account(name=account_name,account_type=account_type)
      dao.save_account(account)
      return account

    def reverse_account(self, account_id=None):
      'reverses all the transactions of the account'
      pass

    def transfer_fund(self, debit_account=None, \
      credit_account=None, amount=None, file=None):
      'transfer funds, basically records the transaction one at a time'
      dao = AMSDao()
      current_time = time.localtime()
      transation = Transaction(debited_account=debit_account, credited_account=credit_account,\
      amount=amount, date=Time(month=current_time.tm_mon, day=current_time.tm_mday, \
        year=current_time.tm_year))
      dao.save_transaction(transation)
      return True

    def view_journal(self, from_date=None, to_date=None):
      pass

    def view_transctions_balance_account(self, account=None, to_date=None, \
      from_date=None):
      pass

    def view_ledger():
      pass

    def generate_profit_loss_statement(self, from_date=None, to_date=None):
      pass

    def generate_balance_sheet(self, as_of_date=None):
      pass

  # the instance is None for the first time
  # check if this is none while assigning instance,
  # else just return the previous instance, so that we have just one 
  # instance of the object at all times.
  # since the instance is a class variable, it is made just once for the 
  # class rather than for the instances.

  # __new__(cls) creates the object for the class, takes cls as the argument
  # where as __init__(self) initializes the created object.
  # so, basically __new__(cls) is the constructor analogy in Python.

  instance = None

  def __new__(cls):
    'creates the AMSService object'
    if not cls.instance:
      cls.instance = cls.__AMSService()
    return cls.instance

  def __init__(self):
    pass



# Class for AMSDao
# just trying out the singleton pattern without using the __new__(cls)
# function, the below definition doesn't do a goof job at making singleton
# objects. Need to stick with the __new__(cls) function
# class AMSDao(object):
#   'AMS Dao class'
#   class __AMSDao(object):
#     'private inner class for AMS Dao class'
#     def __init__(self):
#       pass

#   instance = None

#   def __init__(self):
#     if not AMSDao.instance:
#       AMSDao.instance = AMSDao.__AMSDao()
#     else:
#       # AMSDao.instance.val = arg
#       pass





