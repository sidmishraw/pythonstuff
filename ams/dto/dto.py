# dto.py
# Has the Data Transfer Objects for AMS
'Module for DTOs of AMS'

__author__ = 'sidmishraw'

from ams.utils.utils import Time
from ams.utils.utils import Money


# Journal
class Journal(object):
  'Journal DTO'

  # Since this is a DTO, it doesn't hurt to have the
  # open access to the attributes
  def __init__(self, from_date, to_date, entries=None):
    'initializes Journal DTO \
     from_date - Time \
     to_date - Time \
     entries - list(Transaction)'

    if not (type(from_date) is Time or type(to_date) is Time \
      type(entries) is list):
      raises AttributeError('Wrong types used for the attributes')

    self.from_date = from_date
    self.to_date = to_date
    self.entries = entries


# ProfitLoss statement
class ProfitLossStatement(object):
  'ProfitLoss statement DTO'
  pass

# BalanceSheet
class BalanceSheet(object):
  'Balance Sheet DTO'
  pass

# AccountSummary
class AccountSummary(object):
  'Account Summary DTO'
  pass

# Ledger
class Ledger(object):
  'Ledger DTO'
  pass
