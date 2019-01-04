#!/usr/bin/python
 
import urllib2
 
for line in urllib2.urlopen('http://www.wechall.net/challenge/training/get_sourced/index.php'):
  if "password:" in line:
    print line
