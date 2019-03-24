Python Beyond the Basics
==========================

Pluralsight  Robert Smallshire, Austin Bingham


chapters
ch 
01 prepreqs
02 organizing larger programs
03 beyond basic funcs
04 closuers and decorators
05 properties and metnds
06 strings and representations
07 numeric and scalar types
08 iterables and iteration
09 inheritance and subtype polymorphism
10 implementing collections,
11 exception and errors
12 definting context managers,
13 introspection
==================


ch 2 organize larger progs
===========================
python
>>import urllib
>>import urllib.request
>>> urllib.__path__
['/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib']
>>> urllib.request__path__
no such attribute

## how python import modules
python
>>> import sys
>>> sys.path    #outputs list of folders where python looks for a module
>>sys.path[0)  #outputs '' meaning current directory
>>>>> sys.path[-2:]  #tail of this list normally is where 3rd party modules are installed

#how to import code not in path
mkdir not_searched
in not_searched crate file path_test.py with method  def found()
python
>>> import path_test
ModuleNotFoundError: No module named 'path_test'
>> import sys
>>sys.path.append('not_searched')
>>sys.path
>>import path_test #now works
>>> path_test.found() ##works

#2. you can add new paths to env variable PYTHONPATH  which gets appended to sys.path
export PYTHONPATH=not_searched
python
>>import path_test #works

### imlement a package
mkdir reader
touch reader/__init__.py

