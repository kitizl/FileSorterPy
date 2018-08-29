#!python3

import os
import sys
import re
import glob
import shutil

START_FOLDER = os.getcwd()

def numToMonth(number):
	return ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][number-1]

def getDate(filename):
	# filename = yyyymmdd-nnnnnn
	date = re.findall(r"(\d{4})(\d{2})(\d{2})\_\d{6}",filename)[0]
	return (date[0],numToMonth(int(date[1])),date[2])

def createFolder(path):
	if not os.path.exists(path):
		os.mkdir(path)
	os.chdir(path)

def createTree(filename):
	date_data = getDate(filename)

	yypath = os.path.join(".",date_data[0])
	# create yy if not exists
	createFolder(yypath)

	mmpath = os.path.join(".",date_data[1])
	# create mm if not exists
	createFolder(mmpath)

	ddpath = os.path.join(".",date_data[2])
	# create dd if not exists
	createFolder(ddpath)

	# The "." was added in the paths because the directory will be changed anyway
	return os.getcwd()

def movefiles():
	# return list of files in the folder
	filelist = [f for f in glob.glob("*.???*")]
	for file in filelist:
		currentpath = createTree(file)
		# move each file from folder_path to finalpathstring
		shutil.move(os.path.join(START_FOLDER,file),os.path.join(currentpath,file))
		# go back to main folder_path
		os.chdir(START_FOLDER)

	return "Success"


# running the code below
movefiles()