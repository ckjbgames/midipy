#!/usr/bin/env python
# midilib.py
def hexchr(hexa):
    return chr(int(hexa,16))
class midi(object):
    def __init__(self, fname, tracks):
        self.midifile = open(fname,'a+')
        self.midifile.write('MThd')
class trackevent(object):
    messages = {'noteon' : '90',
                'noteoff' : '80',
                'aftertouch' : 'A0',
                'contcontroller' : 'B0',
                'patchchange' : 'C0',
                'chanpressure' : 'D0',
                'pitchbend' : 'E0'}
    
