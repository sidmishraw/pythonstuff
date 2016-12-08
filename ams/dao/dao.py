# dao.py
# DAO class for AMS

'Module for dao for AMS'

__author__ = 'sidmishraw'


# making AMSDao a singleton
class AMSDao(object):
  'AMS Dao class'

  class __AMSDao(object):
    'private inner class for AMS Dao class'

    # creating a list and dict to back the inmemory storage for
    # transactions and accounts
    __transaction_dict = {}
    __account_dict = {}

    def __init__(self):
      pass

    # made all methods to be class functions, since they need to
    # access the class variables(dicts)

    def save_account(cls,account):
      'saves the account to the account dict'

      cls.__account_dict[account.get_account_ID()] = account

    def save_transaction(cls, transaction):
      'saves the transaction to the transaction dict'

      cls.__transaction_dict[transaction.get_transaction_ID()] = transaction

    def get_account(cls,accountID):
      'fetches the account for the given account ID'

      return cls.__account_dict[str(accountID)]

    def get_transactions(cls,from_date, to_date):
      'fetches a list of all transactions from_date to to_date'
      transactions = []

      for transaction in cls.__transaction_dict.values():

        if from_date <= transaction.get_date() <= to_date:

          transactions.append(transaction)

      return transactions

    def get_all_accounts(cls):
      'fetches the list of all accounts'

      return list(cls.__account_dict.values())

    def get_all_transactions(cls):
      'fetches the list of all transactions'

      return list(cls.__transaction_dict.values())

    def get_transactions_till_now(cls,till_date):
      'fetches the transactions till now'
      transactions = []

      for transaction in cls.__transaction_dict.values():

        if transaction.get_date() <= to_date:

          transactions.append(transaction)

      return transactions

    def get_transactions_from_date(cls,from_date):
      'fetches the transactions from a particular date'
      transactions = []

      for transaction in cls.__transaction_dict.values():

        if from_date <= transaction.get_date():

          transactions.append(transaction)

      return transactions

  # used for making the AMSDao a singleton class
  instance = None

  # I'm basically creating just one instance of the 
  def __new__(cls):
    'creates the object for AMSDao'
    if not AMSDao.instance:
      AMSDao.instance = AMSDao.__AMSDao()
    return AMSDao.instance

  def __init__(self):
    pass
