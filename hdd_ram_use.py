#!/usr/bin/env python
import os as OS

def getRAMRaw():
    p = OS.popen('free')
    i = 0
    while True:
        line = p.readline()
        if i==1:
            return(line.split()[1:4])
        i += 1

def getDiskUseRaw():
    lines = OS.popen('df')
    i = 0
    for line in lines:
        if i == 1:
            return(line.split()[1:4])
        i += 1

def getRAMFormat(index = 'free'):
    total,use,free = getRAMRaw()
    if index == 'total':
        return(int(total) / 1024)
    elif index == 'use':
        return(int(use) / 1024)
    else:
        return(int(free) / 1024)


def getDiskUseFormat(index = 2, size = 'M'):
    total,used,free = getDiskUseRaw()
    value = 0
    if index == 0:
        value = total
    elif index == 1:
        value = used
    else:
        value = free

    if value == 0:
	return(0)

    if size == 'K':
        value = int(value)
    elif size == 'G':
        value = round(float(value) / 1024 / 1024, 2)
    else:
        value = int(value) / 1024

    return(value)

# Usege:
#print( 'Free RAM: ' + str(getRAMFormat()))
#print( 'Free HDD: ' + str(getDiskUseFormat(1,'G')))
