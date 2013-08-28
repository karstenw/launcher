Launcher
========

Appscript/py2app demo that allows time delayed start of other applications and documents.

This originated long ago from the "MiniTC" demo that used to be part of an appscript tutorial (v0.18.1)


## Download ##
Downloads at my dropbox: http://goo.gl/PXJwFw


## Compiling ##

#### Prerequisites for compiling: ####


+ Apple developer tools
+ python 2.7 - older versions may work
+ py2app
+ appscript


Please do not use the system python. Download the latest 2.7 32-bit version at python.org.


## Short description ##


Copy the downloaded app to the Applications folder

The app implements one AppleScript command: 

- launchAppWithDelay

which has one text parameter which consists of 3 lines:

1. line: Unix path to an application

2. line: Unix path to a document to be opened by the ap from path 1

3. line: Delay in seconds.

Have a look at the accompanied AppleScript "test_launchwithdelay". The initial use was for a FileMaker forum where the task was to restart the database after a specified
amount of time.

When using this from FileMaker to restart itself, the parameter can be calculated
with this:

```
/* posix application path */
"/Volumes"
& Get ( FileMakerPath )
& If (PatternCount( Get ( ApplicationVersion ); "Advanced")>0 ;
    "Filemaker Pro Advanced.app¶";
    "Filemaker Pro.app¶") &

/* posix document path */
Substitute( Get ( FilePath ); "file:"; "/Volumes")  &"¶" &

/* time to wait */
"4.0"
```

And the "Send Event" call should be configured with:
+ Event Class: KWFL
+ Event ID: LAWD

