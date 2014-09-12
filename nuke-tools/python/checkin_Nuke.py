import sys, os, glob
import utilities as amu
import nuke
#from common_Nuke import *

def checkin():
	save = nuke.scriptSave()
	if save==True:
		toCheckin = get_checkin_path()
		if can_checkin():
			amu.setComment(toCheckin, 'comment')
			dest = amu.checkin(toCheckin)
			nuke.message('Checkin Successful!')
			nuke.scriptClear()
		else:
			nuke.message('Can not check in')

def go():
	checkin()

def get_file_path():
    return nuke.callbacks.filenameFilter( nuke.root().name())

def get_checkout_path():
	return os.path.basename(os.path.dirname(get_file_path()))

def get_checkin_path():
	filePath = get_file_path()
	return os.path.join(amu.getUserCheckoutDir(), os.path.basename(os.path.dirname(filePath)))

def can_checkin():
	toCheckin = get_checkin_path()
	#nuke.message(toCheckin)
	return amu.canCheckin(toCheckin)
