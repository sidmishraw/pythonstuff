# dao.py
# DAO class for AMS

'Module for dao for AMS'

__author__ = 'sidmishraw'

# making AMSDao a singleton
class AMSDao(object):
  'AMS Dao class'
  class __AMSDao(object):
    'private inner class for AMS Dao class'
    def __init__(self):
      pass

  instance = None

  # I'm basically creating just one instance of the 
  def __new__(cls):
    'creates the object for AMSDao'
    if not AMSDao.instance:
      AMSDao.instance = AMSDao.__AMSDao()
    return AMSDao.instance

  def __init__(self):
    pass
