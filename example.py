# example.py
# script for testing my AMS

__author__ = 'sidmishraw'

# Always use absolute names for the packages, prevents problems 
# due to faulty paths
# Never try to modify PYTHONPATH or sys.path for imports, it is 
# the wrong way of doing things. Only do that if no other alternative
# can be found.(patch-work)
from ams.utils.utils import Money
from ams.utils.utils import Time
from ams.constants.constants import AccountType
from ams.bo.bo import *
from ams.service.service import *
from ams.dao.dao import *

if __name__ == '__main__':
  print('Running example for AMS')
  a = Money(amount=12114314.333)
  b = Money("INR", amount=132143143.1899)
  t = Time(month=12,day=23,year=2016)
