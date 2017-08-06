#!/usr/bin/python3

##########################################
# Project: Python MultiLanguage System   #
# Author: Aninu                          #
##########################################

import imp
import sys

# Variable
LangFile = ''
LangDefault = ''
LangList = []
LangArray = []

# Functions
class Lanuage:
	def __init__(self, location = ''):
		global LangFile, LangDefault, LangArray, LangList
		sys.path.append(location)
		import lang_settings as settings
		if (location):
			LangFile = location + "/" + settings.LangFile
		else:
			LangFile = settings.LangFile
		LangDefault = settings.LangDefault
		LangArray = settings.LangArray
		LangList = settings.LangList

	def Lang_CheckIfExist(Lang):
		fLang = 0
		for tag in LangList:
			if (tag == Lang):
				fLang = 1
				break
		return fLang

	def Lang_Load(Lang):
		if (Lanuage.Lang_CheckIfExist(Lang)):
			return LangArray[Lang]
		else:
			return LangArray[self.LangDefault]

	def Lang_SetUserLanguage(Lang):
		file = open(LangFile, 'w')
		file.write(Lang)
		file.close()
		return 0

	def Lang_Set(Lang):
		for tag in LangList:
			if (tag == Lang):
				Lanuage.Lang_SetUserLanguage(Lang)
				break
		return 0

	def Lang_GetUserLanguage():
		try:
			file = open(LangFile, 'r')
			lang = file.read()
			file.close()
			if (lang):
				return lang
			else:
				return LangDefault
		except:
			return LangDefault

	def Lang_GetText(Pos):
		Lang = Lanuage.Lang_GetUserLanguage()
		try:
			return Lanuage.Lang_Load(Lang)[Pos]
		except:
			return ""

	def Lang_GetDefault():
		return LangDefault

# Small tag
setL = Lanuage.Lang_SetUserLanguage
getL = Lanuage.Lang_GetText
getDef = Lanuage.Lang_GetDefault()

##### END
