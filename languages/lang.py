#!/usr/bin/python3

##########################################
# Project: Python MultiLanguage System   #
# Author: Aninu                          #
##########################################

import imp
import sys

sys.path.append("languages")

import lang_settings as settings

# Functions
def Lang_CheckIfExist(Lang):
	fLang = 0
	for tag in settings.LangList:
		if (tag == Lang):
			fLang = 1
			break
	return fLang

def Lang_Load(Lang):
	if (Lang_CheckIfExist(Lang)):
		return settings.LangArray[Lang]
	else:
		return settings.LangArray[settings.LangDefault]

def Lang_SetUserLanguage(Lang):
	file = open(settings.LangFile, 'w')
	file.write(Lang)
	file.close()
	return 0

def Lang_Set(Lang):
	for tag in settings.LangList:
		if (tag == Lang):
			Lang_SetUserLanguage(Lang)
			break
	return 0

def Lang_GetUserLanguage():
	try:
		file = open(settings.LangFile, 'r')
		lang = file.read()
		file.close()
		if (lang):
			return lang
		else:
			return settings.LangDefault
	except:
		return settings.LangDefault

def Lang_GetText(Pos):
	Lang = Lang_GetUserLanguage()
	return Lang_Load(Lang)[Pos]

def Lang_GetDefault():
	return settings.LangDefault

# Small tag
setL = Lang_SetUserLanguage
getL = Lang_GetText
getDef = Lang_GetDefault()

##### END
