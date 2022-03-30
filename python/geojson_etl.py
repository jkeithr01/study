#!/usr/bin/python

#PROGRAM: GeoJSON ETL
#AUTHOR: J. Keith Ratliff
#CREATED: 20170731
#VERSION: 1.0
#LASTMODIFIED: 20170807
#DESCRIPTION:
# This program shall read a data collection from the 
# U.S. Geological Survey (Dept of Interior) at http://www.usgs.gov/
# transform that data set into a format that is readable by a variety of 
# Hadoop ecosystem tools.
# More specifically, the data comes in JSON format, but the file format 
# is not one record  per line. Both the first and last lines contain 
# additional information that are not specifically earthuake data records.
#
# The first line contains a metadata description and also the character 
# sequence that begins the record collection:
# {"type":"FeatureCollection","metadata":{"generated":1503416240000,
# "url":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson",
# "title":"USGS Magnitude 2.5+ Earthquakes, Past Day",
# "status":200,"api":"1.5.8","count":33},
# "features":[   <-- This character sequence begins the record collection.
# 
# The last line simply closes the "FeatureCollection" by closing the last 
# record, then closing the collection. This line also contains one additional 
# collection attribute, "bbox":
# ],   <-- This character sequence ends the record collection
# "bbox":[-178.5237,-17.6923,0.2,178.3742,71.768,532.4]}
#
# Each record in the dataset is an element of type "Feature" 

# Combining URLLib2 and JSON modules to read data from the 
# U.S. Geological Survey (Dept of Interior) at http://www.usgs.gov/
# Specifically, the examples here use the JSON summary feed of earthquake data
# See details here: https://earthquake.usgs.gov/earthquakes/feed/
#
import urllib2
import json
## The URL for earthquake data from the last day where the quake measured >2.5
## on the moment magnitude scale (MMS, a successor of the Richter scale)
feedurl = 
  'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
dataURL = urllib2.urlopen(feedurl)
# respCode = '404'
respCode = str(dataURL.getcode())
if (respCode == '200'):
	print 'Got code ' + respCode + '... continuing processing of data.'
	content = dataURL.read()
	jsonData = json.loads(content)
	if "title" in jsonData["metadata"]:
		print jsonData["metadata"]["title"]
	if "count" in jsonData["metadata"]:
		count = jsonData["metadata"]["count"]
		print str(count) + " events recorded."
	for item in jsonData["features"]:
		print "Mag: %6.3f" % item["properties"]["mag"] , " at ", item["properties"]["place"]
else:
	print 'Got a bad code:' + respCode



