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

import pdb
import pprint
pp = pprint.pprint

kwdbg = True

def waitAndLaunch(params):

    if u'\r' in params:
        path, doc, seconds = params.split(u'\r', 2)
    else:
        path, doc, seconds = params.split(u'\n', 2)

    if kwdbg:
        pp(params)

    try:
        seconds = float( seconds )
    except Exception, err:
        print
        print err
        seconds = 0.0
    if seconds:
        time.sleep( seconds )

    docpath = mt.File( doc )

    if os.path.exists( path ):
        fmp = app( path )
        # fmp.launch()
        fmp.run()
        fmp.activate()
        time.sleep( 3 )
        if os.path.exists( doc ):
            fmp.open( docpath.alias )
    else:
        finder = app("Finder.app")
        finder.open( docpath.alias )

def openapp():
    app("").activate()
    time.sleep(2)

    

# open all
installeventhandler(openapp, 'aevtoapp')
installeventhandler(lambda front=True:None, 'aevtrapp', ('frnt', 'front', '****'))
installeventhandler(lambda:QuitApplicationEventLoop(), 'aevtquit')

installeventhandler(
    waitAndLaunch,
    'KWFLLAWD',
    ('----', 'params', kAE.typeUnicodeText) )


if __name__ == '__main__':
    RunApplicationEventLoop()
