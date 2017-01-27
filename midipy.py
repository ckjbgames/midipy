#!/usr/bin/env python
# midilib.py
def hexchr(hexa):
    return chr(int(hexa,16))
class midi(object):
    # Event definitions (in hexadecimal)
    trackevents = {'seq_number' : '00',
                   'txtevent' : '01',
                   'trackname' : '03',
                   'instrument' : '04'}
    def __init__(self, fname, tracks):
        self.midifile = open(fname,'a+')
        self.midifile.write('MThd')
