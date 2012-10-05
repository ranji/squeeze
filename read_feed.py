#!/usr/bin/env python
# encoding: utf-8
"""
read_feed.py

Created by ranji on 2012-09-25.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import feedparser
import re
import time
import datetime
import subprocess
from bcolors import bcolors

def main():
	prev_state = {}
	current_state = {}
	rss_url="http://teamcity.bridgepoint.local/guestAuth/feed.html?projectId=project4&buildTypeId=bt18&buildTypeId=bt24&buildTypeId=bt12&buildTypeId=bt14&buildTypeId=bt9&buildTypeId=bt6&buildTypeId=bt19&buildTypeId=bt22&buildTypeId=bt20&buildTypeId=bt13&buildTypeId=bt11&buildTypeId=bt10&projectId=project3&buildTypeId=bt5&buildTypeId=bt21&itemsType=builds&buildStatus=successful&buildStatus=failed&userKey=guest"

	sorted_entries = get_sorted_entries(rss_url)
	prev_state = get_latest(sorted_entries)
	while 1:
		sorted_entries = get_sorted_entries(rss_url)
		current_state = get_latest(sorted_entries)
		for key,value in current_state.iteritems() :
			if value != prev_state[key]:
				notify(key,prev_state[key],value) 
		prev_state = current_state
		time.sleep(10)

def play_text(txt):
        subprocess.call('echo '+txt+' | festival --tts',shell=True)
				
def play_mp3(paths):
	for path in paths:
		subprocess.call("mpg123 "+path,shell=True)
			
def notify(build,prev,curr):
	if prev == 'failed' and curr == "passed":
		good_status = build +' status changed from failed to passed'
		print bcolors.OKBLUE + good_status
		play_good()
		play_text(good_status)
	else:
		failed_status = build +' status changed from passed to failed'
		print bcolors.FAIL + failed_status
		play_bad()
		play_text(failed_status)
	
		
def get_latest(sorted_entries):
		print 'current buid status:'
		print datetime.datetime.now()
		
		print '-----------------------------------------------'	
		latest = {}
		for entry in sorted_entries:
			key = ""
			r = re.compile('::(.*?) #')
			m = r.search(entry["title"])
			if m:
			    key = m.group(1)
			
			if not key in latest:
				if 'failed' in entry["title"]:
					latest[key] = 'failed'
				else: 
					latest[key] = 'passed'
				print (bcolors.OKGREEN if 'passed' in latest[key] else bcolors.FAIL) + key + " - "+latest[key]
						
		print '----------------------------------------------'
		return latest;
		

def get_sorted_entries(rss_url):
	feed = feedparser.parse( rss_url )
	entries = []
	entries.extend( feed[ "items" ] )
	sorted_entries = sorted(entries, key=lambda entry: entry["published"])
	sorted_entries.reverse() # for most recent entries first
	return sorted_entries;
	
def play_bad():	
	paths = []
	paths.append('sounds/BabyCry.mp3')
	play_mp3(paths)

def play_good():
	paths = []
	paths.append('sounds/Dijjeridoo.mp3')
	play_mp3(paths)

def play_sounds(paths):
	for path in paths:
		play_sound(path)

		
if __name__ == '__main__':
	main()

