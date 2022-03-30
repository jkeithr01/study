#!/usr/bin/python

#PROGRAM: Python Hello World
#AUTHOR: J. Keith Ratliff
#CREATED: 20170731
#VERSION: 1.0
#LASTMODIFIED: 20170823

# defining a function that returns a value
def greet():
	return "Hello!"

# defining a function that takes arguments
def greetWithName(name="User"):
	return "Hello, " + name + "!"

def main():
	print "Hello, world!"
	print "\nDemonstrating basic function definitions and calls..."
	print "Executing greet..."
	print greet
	print greet()
	print greetWithName
	print greetWithName()
	print greetWithName("Keith")
   	# The following 2 line generate errors.
	#	print notThisOne
	#	print notThisOne()
	print "This is the end of the main() function."
	raw_input("Press <Enter> to continue: ")

if __name__ == "__main__":
	main()

# Functions have to be defined before you call them
# I can't define this fuction here and expect main() above to be able to call it.
# def notThisOne():
#	print "I don't seem to work"

# Program execution is not bound by the main() function
# The execution thread resumes here after the call to main above

# 
# Variables and assignments
#
# Python is a dynamically typed language.
# Variables are not typed by declaration, but they do need to be assigned.
# Variables can be reassigned and given a new type when reassigned.
print "\nDemonstrating variable declaration, assignment, and printing..."
a = 25
b = 4
c = a * b
print "The value of 'a' is %d" % a
print "The value of 'b' is %d" % b
print "The value of 'c' is %d" % c
resp = raw_input("Press <Enter> to continue: ")
print ""

c = "Now 'c' is a string"
print c
resp = raw_input("Press <Enter> to continue: ")
print ""

# 
# Program control structures
#
# Conditional execution is handled using the if..elif..else construct.
# It mirrors the if..elif..else..fi construct in bash programming and also mirrors 
# the if..else if..else construct from C/C++/Java type syntax.
print "An if statement demo:"
x = 0
if (x < 0):
	print "x is negative"
elif (x == 0):
	print "x is zero"
else:
	print "x is positive"
# Looping
# There are only two type of loops in Python: while... and for...
## The while loop is a conditional testing loop:
print "A while loop demo:"
x = 0 
while (x<5):
	print x
	x =  x + 1
## The for loop is an iterator-based loop:
print "A for loop demo:"
for x in range(0,5):
	print x
## Using a for loop to iterate over a collection:
print "A for loop demo of iterating over a collection:"
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print days
for day in days:
	print day

#
# Classes
# 
# Classes can be created in Python much like other object-oriented and object-aware environments
print "\nDefininng and using classes demo:"
class MyClass():
	name = "MyClass"
	# All class methods take "self" as a first parameter
	# The "self" variable corresponds to the "this" reference from C++ and Java.
	# It is a self-referential  that object instances use to access instance members.
	# This parameter is populated by the system automatically.
	def method1(self):
		print "This is method1. It takes no arguments."

	def rename(self, newName = "MyClass"):
		self.name = newName
		print "My new name is ",self.name

c = MyClass()
print "The new object c is named ",c.name
c.method1()
c.rename("Fred")
# You can use the self reference and class-level method definitions to call instance-specific methods,
# unlike in Java (or C++ that I know of).
MyClass.rename(c,"Barney")

#
# Date and Time utilities
# 
print "\nDate and Time utility demo:"
## Import necesary library components
from datetime import date
from datetime import time
from datetime import datetime
## Create a datetime object from current time and print it
current_datetime = datetime.now()
print "The current datetime value is: " + current_datetime.isoformat()
print "The date is " + current_datetime.strftime("%A, %B %d, %Y")
## Using the calendar library
import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
yr =  current_datetime.year
mo = current_datetime.month
calstring = cal.formatmonth(yr,mo)
print calstring
## THere's also a HTML calendar for creating HTML table calendars
htmlcal = calendar.HTMLCalendar(calendar.SUNDAY)
htmlcalstring = htmlcal.formatmonth(yr,mo)
print htmlcalstring

# 
# Files and File I/O
#
# File I/O in Python is based on C's stdio library
#
## Note that the file  object is built in, so no import is required
## This can be verified by executing 'dir(__builtins__)' in the python shell
##
## Opening a file
## File modes include the following: r (read, the default value), w (write), a (append)
## File modes can also create the file if  '+' is appended to the mode
## File modes can read test (the default) or binary (by appending 'b' to the mode, e.g., 'rb')
## File modes also support use of a universal EOL marker indicator, 'U'
print '\nTesting file I/O functionality:'
filename = 'testfile.txt'
mode = 'r'
myfile = open(filename,mode)
for line in myfile.readlines():
	print line
## Using the 'os' module
print '\nDemo of os module functions:'
import os
print os.name
from os import path
filepath = path.realpath(filename)
print path.dirname(filepath)

# Using URLLib2 to access Internet content
#
## Open and read information from a web site
print '\nDemo of URLLib functions:'
import urllib2
siteURL = 'http://www.ratliffs.net/'
webURL =  urllib2.urlopen(siteURL)
print 'The response code was ' + str(webURL.getcode())
print webURL.read()

# Combining URLLib2 and JSON modules to read data from the 
# U.S. Geological Survey (Dept of Interior) at http://www.usgs.gov/
# Specifically, the examples here use the JSON summary feed of earthquake data
# See details here: https://earthquake.usgs.gov/earthquakes/feed/
#
import urllib2
import json
## The URL for earthquake data from the last day where the quake measured >2.5
## on the moment magnitude scale (MMS, a successor of the Richter scale)
feedurl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
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



