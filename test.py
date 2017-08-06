#!/usr/bin/python3

##########################################
# Project: Python MultiLanguage System   #
# Author: Aninu                          #
##########################################

import languages.lang as myLang

# Init
myLang.Lanuage('languages')

# Set Lang RO
myLang.setL('ro')
print (myLang.getL(0))
print (myLang.getL(1))
print ()

# Set Lang EN
myLang.setL('en')
print (myLang.getL(0))
print (myLang.getL(1))
print ()

# Set Lang FR
myLang.setL('fr')
print (myLang.getL(0))
print (myLang.getL(1))
print ()

# Set Lang IT
myLang.setL('it')
print (myLang.getL(0))
print (myLang.getL(1))
print ()
