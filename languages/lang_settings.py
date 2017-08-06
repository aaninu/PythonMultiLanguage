#!/usr/bin/python3

##########################################
# Project: Python MultiLanguage System   #
# Author: Aninu                          #
##########################################

import lang_ro as ro
import lang_en as en
import lang_fr as fr
import lang_it as it

# File for save
LangFile = 'lang.txt'

# Default lang
LangDefault = "en"

# List with language
LangList = {
	'ro': "Română",
	'en': "English",
	'fr': "Français",
	'it': "Italiano",
}

# Lang Array
LangArray = {
	'ro': ro.LangArray,
	'en': en.LangArray,
	'fr': fr.LangArray,
	'it': it.LangArray,
}

