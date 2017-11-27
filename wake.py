#!/usr/bin/env python
# coding: utf-8

from time import time, sleep

class alarmClock():
	def __init__(self, targetTime=None, sleepTime=None):
		'''
		@targetTime Sets the target time to trigger alarm
		@sleepTime Sets the alarm to trigger after the elapsed sleepTime
		'''
		assert targetTime != None or sleepTime!=None, "You must provide a time to wake up or a sleep duration."
		if targetTime: assert type(targetTime) == sleepTime == None, "You must only provide targetTime or sleepTime."
#		if sleepTime: assert if targetTime: self.targetTime = targetTime
#		print self.targetTime #this is to remove afterwards

def setAlarm(sleep):
	sleep(sleep)
	# insert opening of a link to video

def timeDelta(duration):
	currTime = time()
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
'''
if __name__ == "__main__":
	import sys
	sys.argv[1]
'''
print minutesToSeconds(1)
print hourToSeconds(1)