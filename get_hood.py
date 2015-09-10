# Denis Balobin
# a module for determining what neighborhood in NYC
# the user is in
# you can obtain user's latitude and longitude values 
# using Google's geolocation

import neighborhoods

# import hoodList from neighborhoods.py
hoodList = neighborhoods.hoodList
nycBounds = neighborhoods.nycBounds

# takes a list someList containing polygon edge values
# and a point somePoint. returns 1 if the polygon
# contains the point and -1 if it does not
# it basically checks if the given point
# lies to the left of every edge of the polygon
# that encloses an NYC neighborhood.
def containsPoint(someList, somePoint):
		i = 0
		for aTuple in someList:
			a = -(aTuple[1][1] - aTuple[0][1])
			b = aTuple[1][0] - aTuple[0][0]
			c = -((a * aTuple[0][0]) + (b * aTuple[0][1]))
			d = (a * somePoint[0]) + (b * somePoint[1]) + c
			if d < 0:
				return -1
			else:
				continue
		return 1

# simple function that determines if current location
# is within the bounds of the NYC neighborhoods
# modify it to suit your needs
def getHood(latitude, longitude):
	for hood in hoodList:
		if containsPoint(hood.tupleList, (latitude, longitude)) > 0:
			theHood = hood.name
			print theHood # this is the name of the neighborhood the user is in
			return 0
	if containsPoint(nycBounds.tupleList, (latitude, longitude)) > 0:		 
		print "You are in NYC!"
	else:
		print "You are not in NYC"
