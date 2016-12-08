# exception.py
# Custom Exceptions for AMS

__author__ = 'sidmishraw'

class NotSameCurrencyException(Exception):
  '''
    Raised when the Curreny of 2 money instances are not same
  '''
  pass

class UnbalancedTransactionException(Exception):
  '''
    Raised when the transaction is not balanced
  '''
  pass

class SaveFailedException(Exception):
  pass

class AccountNotFoundException(Exception):
  pass
