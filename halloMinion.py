#!/usr/bin/env python
"""Return the lastseen time of every minion on the salt master.

Usage:
./haloMinion.py
"""
from os import listdir
from os.path import isdir
import datetime
import os
import os.path


def modification_date(filename):
    """Return the modification time of a file"""
    time = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(time)

def datetime2string(i):
    """Return a nice string for a time"""
    return i.strftime("%Y.%m.%d %H:%M:%S")

##########################################################################

DIRECTORY_PKI = '/etc/salt/pki/master/minions/'
'''
This directory stores all keys of known minions.
'''

DIRECTORY_CACHE = '/var/cache/salt/master/minions/'
'''
There are more directories than there are known minons
In each directory there are two files.
'''

##########################################################################

KNOWN_MINIONS = [f for f in listdir(DIRECTORY_PKI) if isdir(DIRECTORY_PKI)]

for one_minion in KNOWN_MINIONS:
    one_minion_cache_dir = os.path.join(DIRECTORY_CACHE, one_minion)
    if isdir(one_minion_cache_dir):
        try:
            age_of_d = modification_date(os.path.join(one_minion_cache_dir, 'data.p'))
        except:
            age_of_d = datetime.datetime.fromtimestamp(0)
        
        try:
            age_of_m = modification_date(os.path.join(one_minion_cache_dir, 'mine.p'))
        except:
            age_of_m = datetime.datetime.fromtimestamp(0)
        lastseen = max(age_of_d, age_of_m)
        print datetime2string(lastseen) + "\t" + one_minion
