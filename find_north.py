# find_north.py
# This is a script as presented in the talk
# https://www.youtube.com/watch?v=RrPZza_vZ3w&index=1&t=99s&list=PLwkaIKb21zdNP5-8rGNVPsCUmdxtpQ1Rn
# regarding learning python through public data hacking
# Find all buses that are travelling northbound of Dave's office

__author__ = 'Sidharth Mishra<sidmishraw@gmail.com>'

# defining global constants -- Dave's lat, long coordinates
daves_latitude = 41.98062
daves_longitude = -87.668542

# import parse function from ElementTree module of xml/etree package
from xml.etree.ElementTree import parse
# parse the rt22.xml file and generate the DOM tree and assign the name
# xmldoc to that tree
xmldoc = parse('rt22.xml')

# A generator for the elements for the particular tagname
def parseThroughXML(tagname):
  """
   This function will parse through the DOM tree to find all the elements
   for the tagname  passed to this function as the argument.
  """
  # Convert to string before finding
  tagname = str(tagname)
  print('tagname = %s' % tagname)
  for element in xmldoc.findall(tagname):
    print(repr(element))
    yield element




# The main function that needs to be executed when \
# we run this script as the main module.
def main():
  # parse through the xmldoc and find all the tags with tagname bus
  for bus in parseThroughXML('bus'):
    # parse through the elements of the tag bus and find the value of <lat></lat>
    # findtext returns the value of the xml tag
    lat = float(bus.findtext('lat'))
    # lat is for north and south
    # long is for east-west
    # Buses North bound that lat coordinate > daves_latitude are the ones to track
    if lat > daves_latitude:
      direction_of_bus = bus.findtext('d')
      if direction_of_bus.startswith('North'):
        bus_id = bus.findtext('id')
        print('Bus ID- %s and lat = %f' % (bus_id,lat))


# standard python boilerplate code that executes the module only if
# it is running as the main module
if __name__ == '__main__':    
  print('Starting find_north.py')
  main()
