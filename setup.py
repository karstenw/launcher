from distutils.core import setup
import py2app
from plistlib import Plist
import os

#######

import LauncherVersion

name = LauncherVersion.name
version = LauncherVersion.version
bundle = LauncherVersion.bundle
creator = LauncherVersion.creator
shortCopyright = LauncherVersion.shortCopyright
longCopyright = LauncherVersion.longCopyright

# set to False during development so that application is visible while running;
# set to True for deployment
hide = False


#######

# create resource file

sdpPath = '/usr/bin/sdp'
RezPath = '/Developer/Tools/Rez'

s = "%s -fa %s.sdef;" % (sdpPath, name)
print s
os.system(s)

s = "%s %sScripting.r -o %s.rsrc -useDF;" % (RezPath, name, name)
print s
os.system(s)

#######


setup(
	name = name,
	version = version,
	app=[name + '.py'],
	options = {
		'py2app': {
			'plist': Plist(
				LSUIElement=int(hide),
				NSAppleScriptEnabled = True,
				CFBundleIdentifier = bundle,
                CFBundleName = name,
                CFBundleDisplayName = name,
				CFBundleVersion = version,
				CFBundleShortVersionString = version,
                CFBundleSignature = creator,
                CFBundlePackageType = "APPL",
				CFBundleIconFile = name + '.icns',
                NSHumanReadableCopyright = shortCopyright,
                CFBundleGetInfoString = longCopyright
			),
            'iconfile': './+icons/appicon.icns',
			'resources': [name + '.rsrc', './+icons/appicon.icns']
		}
	}
)
