#!/usr/bin/env python

if __name__ == '__main__':
	import sys
	import getopt
	print getopt.getopt(sys.argv[1:],"h:s:")
	try:
		opts = getopt.getopt(sys.argv[1:],"h:s:")
	except getopt.GetoptError, e:
		print str(e)
	print opts
	print sys.argv[1:]