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
a module is a single python source file !
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


=== implement a package ===

mkdir reader
touch reader/__init__.py
python
>>import reader #works
>>> type(reader)
<class 'module'>
>>> reader.__file__
'/./../reader/__init__.py'
when you import a packaget its __init__.py  file is executed

! demo 02-organize/reader
  is a module folder (it has __init__.py

create reader/reader.py  with a class Reader
python
>>import reader.reader
>>reader.reader.__file__  #to check which source file is imported
>>r = reader.reader.Reader('reader/reader.py'
>>r.read()
>>r.close()

now put into __init__.py
from reader.reader import Reader

this makes Reader to be in top level of reader package
python
>>import reader
>> r = reader.Reader('/tmp/test.txt') #works
>> r.read()

==subpackages==

create a copy of reader folder to creader
mkdir creader/compressed
touch creader/compressed/__init__.py
>> import creader.compressed #works
in creader/compressed add  gzipped.py   bzipped.py
>>> import creader.compressed.gzipped ## all imports work
>>> import creader.compressed.bzipped

now update creader/reader.py  with
extension_map = {}
and Reader.__init()

create 2 tests files on the same level as creader
python3 -m creader.compressed.bzipped test.bz2 data compressed with bz2
python3 -m creader.compressed.gzipped test.gz data compressed with gzip
echo "hello world " > test.txt
python3
>>import creader
>>r = creader.Reader('test.bz2')
>>r.read() #reads a bz2 compessed file
>>r = creader.Reader('test.gz')
>>r.read() #reads a gz compessed file
>>r = creader.Reader('test.txt')
>>r.read() #reads a clear text file
python3 creader_runner.py



##relative imports, absolute formats
 applies to modules in the same package
 relatives imports advised to be avoided
 from .mb import some func
 from ..ma import some_other_func

__all__ in __init__.py

in compressed/__init__.py  #put
from creader.compressed.bzipped import opener as bz2_opener
from creader.compressed.gzipped import opener as gzip_opener
__all__ = ['bz2_opener', 'gzip_opener']

python3
>>from creader compressed import *
this will import the bz2_opener and gzip_opener
i.e. this is a mean to limit exposure of public APIs in packages
>>locals()



=== namespace packages =====

!!demo  farm   as a skeleton for big package
 split over several directories
 under split_farm   bovine and bird both has __init__.py

how to load it
>>>import sys
>>>sys.path.extend(['farm/path1','farm/path2'])
>>>import split_farm
>>>split_farm.__path__  #shows 2 paths
>>> import split_farm.bovine #works
>>> import split_farm.bird
NB! you probably will not develop multi directory packages at all
further doc: peps/pep-0420

todo: executable directories
entry point for python execution
python3 path
can't find '__main__' module in 'path'

!demo ereader
make an executable program from a reader package
cp -r creader  ereader
cd ereader
mkdir ereader
mv * ereader
touch __main__.py
layout:
 ereader
    __main__.py
    ereader
        __init__.py
        reader.py
        compressed

put in __main__.py code to import a ereader and instatiante Reader obj

>python3 ereader test.txt
>python3 ereader test.gz

a conveniet way to bundle and distribute small programs

## same with zip file
cd ereader/
zip -r ../ereader.zip * #creates a zip file
cd ..
python3 ereader.zip test.txt

NB! recommended prject layout

project_name  (this folder is not a packge but contains a package and supporting files)
|-- __main__.py  (if package is an executable program)
|-- project_name  (this is package, same name as project_name dir)
|   |-- __init__.py
|   |-- more_source.py
|   |-- subpackage1     (can include subpackages)
|   |   |-- __init__.py
|   |-- test            (includes a test subpackage as a root of all tests)
|       |-- __init__.py
|       |-- test_code.py
|
|-- setup.py

modules are singletons
! demo  02-organize/registry
cd registry
>python3 registry_runner.py
check registry.py and registry_runner.py


!! review
a module is a python code usually in a single source file
packages are modules that can contain other modules
mplemented as directories containing a special __init__.py file
they can have subpackages   i.e. creader/compressed
packages have __path__ attribute


ch 3 functions overview
===========================

##callable instances
!demo resolver2
python
>>from resolver2 import resolver as res
>>r = res.Resolver()
>>> type(r)
<class 'resolver2.resolver.Resolver'>
>>> r('cern.ch')
'188.184.9.234'

### lambdas
  ( are anonymous funcs)  they cannot be easily tested so must stay simple

!demo lambdas.py
>python lambdas.py

>>>last_name = lambda name,sep=' ': name.split(sep)[-1]
>>> type(last_name)
<class 'function'>
>>> last_name('Ivan Ivanov')
'Ivanov'
>>> last_name('Ivan/Ivanov','/')
'Ivanov'

## detecting callables
>>> callable(last_name)
True
>>> callable('Ivanov')
False
>>>

!demo func_extend_args.py
>python func_extend_args.py

hypervolume() to pass arbitrary number of params
define a list of args in tuple before passing it to a func
trace(f,*args, **kwargs)  demo
zip_tranposed() demo


ch 04 closures and decorators
==============================

!demo sort_by_last_letter.py
 local funcs defined inside local funcs
 !NB at every call  local func is redefined
    demo_sort_by_last_let()
 global, parameters and inner variables are accessible inside local funcs
    demo_accessing_scopes_from_local_funcs()

** closures **
a closur returns a function.
 most common pattern is a factory of specialized functions

!demo raise_to_closure_factory.py
    demo_factory_squares_cubes():
    raise_to closure can produce different functions of raising argument
    to different arguments

!demo enclosing.py
        demo_non_local_variable()
        shows how a local function can modify a variable from higher scope
        use of nonlocal keyword

!demo  make_timer_nonlocal.py
      more practical example of nonlocal to have independent timers


!demo escape_unicode_decor_first.py
    apply an ascii() decorator to functions which return strings

!demo call_count_class_deco.py
    counts the number of calls of a hello() function via CallCount class as decorator

!demo tracer_instance_deco.py
    debugs a call of a function with an instance decorator
    easy switching off/on decorator tracing functionality  via instance attribute

!demo island_maker_multideo.py
    demo_chain_decorator()   2 decorators applied in chain
    demo_decorator_on_class_method a decorator applied on instance method

!demo noop-functools.py
    how to use @functools.wraps(f)  to maintain  f.__name__  f.__doc__
    important to use in decorators to make sure decoraed functions conserve
    their names and help message

!demo demo_argvalidation.py
    perform function argument validation in a decorator
        demo_func_with_arg_validation_via_deco()
    do validation on multiple arguments
        demo_arg_valid_on_several_params()

ch 05 properties and class methods
==============================


! demo props-class-methods subfolder
    shipping.py
    shipping_runner.py

 -------------------------------------------------------------------------
 !NB carefully study source in shipping.py for base and inherited objects
 -------------------------------------------------------------------------
  demo_BaseContainer()
    shows base object is instantiable
    specialized constructors realized in class methods

  demo_DerivedRefrigiratedContainer()
    instantiation of Derived class
    use of inherited class methods for special constructors even if signature changes
    @property for  getter  and @p.setter for setter
    getter and setter properties
    property accessing its parent value

  demo_DoubleDerivedHeatedRefrigeratedShippingContainer()
    property setter accessing its parent value  (used for value validation )

ch 06 strings and representations
=================================

string representatons of objects in python

repr() for class debugging
str() print uses str(object)

reprlib  (prints a subset of huge element)

ascii(),  ord(), chr()

>>> ascii('hello¾')
"'hello\\xbe'"

>>> chr(190)
'¾'
>>> ord('¾')
190

duck  Table class example


