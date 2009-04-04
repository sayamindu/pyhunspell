#!/usr/bin/python
from distutils.core import setup, Extension

main = Extension(	'hunspell', 
			define_macros = [('_LINUX',None)],
			libraries = ['hunspell-1.2'],
			include_dirs = ['/usr/include/hunspell'],
			sources = ['hunspell.c'],
			extra_compile_args = ['-Wall'])

setup(	name = "hunspell",
	version = "0.1",
	description = "Module for the Hunspell spellchecker engine",
	ext_modules = [main])
