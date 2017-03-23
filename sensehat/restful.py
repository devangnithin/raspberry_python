import json
import urllib2
json.load(urllib2.urlopen("http://forecast.weather.gov/MapClick.php?lat=41.9499937&lon=-88.76921290000001&FcstType=json"))
