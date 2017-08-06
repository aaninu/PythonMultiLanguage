# PythonMultiLanguage
Python Multi Language

# Import Module:
import languages.lang as myLang

# Init
myLang.Lanuage('languages')
Note: languages is directory

# Set Language:
myLang.setL('ro')

# Get text from array:
myLang.getL(0)
myLang.getL(1)
...

# Add text on file:
lang_ro.py
lang_en.py
# You can create multiple files
lang_TAG.py

# If you add more files with lang:
1) open file: lang_settings.py
2) Import file: import lang_en as en
import lang_TAG as TAG
3) Default Lang:
LangDefault = "en"
4) Language list:
LangList = {
	...
	'en': "English",
  'TAG': "Full name",
}
5) Language array:
LangArray = {
	...
	'en': en.LangArray,
  'TAG': TAG.LangArray,
}

