#!/usr/bin/python3

##########################################
# Project: Python MultiLanguage System   #
# Author: Aninu                          #
##########################################

import languages.lang as myLang

# Set Lang RO
myLang.setL('ro')
print (myLang.getL(0))

# Set Lang EN
myLang.setL('en')
print (myLang.getL(0))
