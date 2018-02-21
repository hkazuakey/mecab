#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string

def cmd1(str):
	rline = os.popen(str).readlines() 
	retval = rline[0][:-1]
	return retval
    # return os.popen(str).readlines()[0][:-1]

def cmd2(str):
    cstr = cmd1(str)
    return cstr.split ()

setup(name = "mecab-python",
	version = cmd1("mecab-config --version"),
	py_modules=["MeCab"],
	ext_modules = [
		Extension("_MeCab",
			["MeCab_wrap.cxx",],
			include_dirs=cmd2("mecab-config --inc-dir"),
			library_dirs=cmd2("mecab-config --libs-only-L"),
			libraries=cmd2("mecab-config --libs-only-l"))
			])
