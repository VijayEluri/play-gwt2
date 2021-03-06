###############################################################################
# GWT2 Remove - tested[2010-10-07]
#
# [gwt2:remove]
# 
# Remove a GWT Module
#
# @author Vincent Buzzano <vincent.buzzano@gmail.com>
###############################################################################
import sys, os, string, shutil

from pgwt import *

def getCommands():
	return ["gwt2:remove"]

def getHelp():
	return "Remove a GWT Module"

def execute(args):
	application_path = args.get("app").path
	public_dir = args.get("public_dir")
	modules_dir = args.get("modules_dir")
	gwt_path = args.get("gwt_path")
	
	# List all modules
	modulename = functions.askForModule(args, 'remove', False, True)
	
	# delete the  app
	if not os.path.exists(os.path.join(application_path, modules_dir, modulename)):
		print "~"
		print "~ Error: module " + modulename + " not found."
		print "~"		
		sys.exit(1)
	
	# remove module dir
	if os.path.exists(os.path.join(application_path, modules_dir, modulename)):
		shutil.rmtree(os.path.join(application_path, modules_dir, modulename))
	
	# remove module public dir
	if os.path.exists(os.path.join(application_path, public_dir, modulename)):
		shutil.rmtree(os.path.join(application_path, public_dir, modulename))
	if os.path.exists(os.path.join(application_path, public_dir, 'WEB-INF','deploy',modulename)):
		shutil.rmtree(os.path.join(application_path, public_dir, 'WEB-INF','deploy',modulename))
	
	print "~"
	print "~ done"
	print "~"

