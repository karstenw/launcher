#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-

import os
import time

import aem
kAE = aem.kae

import appscript
app = appscript.app

import mactypes as mt

import aemreceive
installeventhandler = aemreceive.installeventhandler

import Carbon.CarbonEvt
RunApplicationEventLoop = Carbon.CarbonEvt.RunApplicationEventLoop
QuitApplicationEventLoop = Carbon.CarbonEvt.QuitApplicationEventLoop

import pprint
pp = pprint.pprint

kwdbg = True

# import pdb


def waitAndLaunch(params):
    """
    
    Try to open the application from line 1 of the parameter with the document
    of line 2 from the parameter after waiting for an amount of seconds from
    the 3rd line.
    
    If line 1 does not point to a valid file in posix format, it tries to open the
    document via the finder.
    
    The parameter consists of 3 lines which should be separated by either \r or \n
    but not both.
    
    The parameter is text bevause it's first use was for FileMaker where it's easier
    to calculate a text parameter than a list.
    """

    # determine line endings
    if u'\r' in params:
        path, doc, seconds = params.split(u'\r', 2)
    else:
        path, doc, seconds = params.split(u'\n', 2)

    # convert seconds to float
    try:
        seconds = float( seconds )
    except Exception, err:
        print
        print err
        seconds = 0.0

    # debugging stuff
    if kwdbg:
        print "APP:", repr( path )
        print "DOC:", repr( doc )
        print "DELAY:", repr( seconds )

    # wait if there was a valid parameter
    if seconds:
        time.sleep( seconds )

    docpath = mt.File( doc )

    if os.path.exists( path ):
        theapp = app( path )
        theapp.run()
        theapp.activate()
        if os.path.exists( doc ):
            theapp.open( docpath.alias )
    elif os.path.exists( doc ):
        finder = app("Finder.app")
        finder.open( docpath.alias )


def openapp():
    app("").activate()
    time.sleep(0.5)


installeventhandler(openapp, 'aevtoapp')
installeventhandler(lambda front=True:None, 'aevtrapp', ('frnt', 'front', '****'))
installeventhandler(lambda:QuitApplicationEventLoop(), 'aevtquit')

installeventhandler(
    waitAndLaunch,
    'KWFLLAWD',
    ('----', 'params', kAE.typeUnicodeText) )


if __name__ == '__main__':
    RunApplicationEventLoop()
