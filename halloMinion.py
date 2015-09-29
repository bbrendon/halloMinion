#!/usr/bin/env python
import sys
from os import listdir
from os.path import isfile
from os.path import isdir
import datetime
import os
import os.path


def modification_date(filename):
    t = os.path.getmtime(filename)
    x = datetime.datetime.fromtimestamp(t)
    return x

def datetime2string(i):
    r = i.strftime("%Y.%m.%d %H:%M:%S")
    return r

##########################################################################

DIR_OF_DIR_pki = '/etc/salt/pki/master/minions/'
'''
Only those Minons are known
'''



DIR_OF_DIR_cache = '/var/cache/salt/master/minions/'
'''
There are more directories than there are known minons
In each directory there are two files.
'''

##########################################################################

all_known_minions = [ f for f in listdir(DIR_OF_DIR_pki) if isdir(DIR_OF_DIR_pki) ]

for one_minion in all_known_minions:
    one_minion_cache_dir = os.path.join(DIR_OF_DIR_cache, one_minion)
    if isdir(one_minion_cache_dir):
        age_of_d = modification_date(os.path.join(one_minion_cache_dir,'data.p'))
        age_of_m = modification_date(os.path.join(one_minion_cache_dir,'mine.p'))
        lastseen = max(age_of_d,age_of_m)
        print datetime2string( lastseen)+ "\t" + one_minion
