import urllib2
import sys

try:
	url = str(sys.argv[1])
	print url
	page = urllib2.urlopen(url).read()
	print page
except:
	print "wrong url" 