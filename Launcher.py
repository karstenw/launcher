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

kwdbg = False

def waitAndLaunch(params):

    if u'\r' in params:
        path, doc, seconds = params.split(u'\r', 2)
    else:
        path, doc, seconds = params.split(u'\n', 2)

    # pp(params)

    try:
        seconds = float( seconds )
    except Exception, err:
        print
        print err
        seconds = 60.0
    time.sleep( seconds )
    apppath = mt.File( path )

    a = mt.File( doc )

    fmp = app( path )
    # fmp.launch()
    fmp.run()
    fmp.activate()
    time.sleep( 3 )
    fmp.open( a.alias )

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
