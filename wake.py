#!/usr/bin/env python
# coding: utf-8

import time

class alarmClock():
	def __init__(self, wakeTime=None):
		'''
		@wakeTime Sets the target time to trigger alarm
		'''
		assert wakeTime != None, "You must provide a wake time."
		self.__startTime = time.localtime()
		self.wakeTime = wakeTime
		while time.time() < self.wakeTime:
			time.sleep(1)
		print time.time(), self.wakeTime #this is to remove afterwards


def setAlarm(sleep):
	time.sleep(sleep)
	# insert opening of a link to video

def timeDelta(duration):
	currTime = time.time()
	wakeTime = currTime + duration
	return wakeTime

def timeToSeconds(time):
	pass

def hourToSeconds(hours):
	minutes = hours*60
	seconds = minutesToSeconds(minutes)
	return seconds

def minutesToSeconds(minutes):
	seconds = minutes*60
	return seconds


if __name__ == "__main__":
	import sys, getopt
	assert len(sys.argv) > 1, 'You must provide at least the intended hour to wake with the -h arguement'
	opts, args = getopt.getopt(sys.argv[1:], 'h:m:')
	print opts
	for opt, arg in opts:
		if opt == '-h':
			pass