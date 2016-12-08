# constants.py
# Contains all the constants for the AMS

__author__ = 'sidmishraw'

# For enum in Python
from enum import Enum

class AccountType(Enum):
  ASSET = 1
  LIABILITY = 2
  STOCKHOLDERS_EQUITY = 3
  REVENUE = 4
  EXPENSE = 5