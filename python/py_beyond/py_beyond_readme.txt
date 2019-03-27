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


===========================
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


==============================
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


===================================
ch 05 properties and class methods
==================================


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

==================================
ch 06 strings and representations
=================================

    !demo point.py
    demo_Point()
        uses of str(obj), repr(obj)
    repr() well suited for debugging, logging
    good idea to always implement __repr__() in classes

    str() is a readable human-friendly representation of an object
    (not programmer oriented)


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

===========================
07 numeric and scalar types
===========================

int # arbitrary precision in python
    other languages 16, 32 64 bits precision
float  64 bit precision  (double in C++, Java )
1 bit - sign
11 birs - exponent
53 bits - fraction or mantissa
i.e. python has 15 to 17 bits of decimal precision

sys.float_nfo show limits of float type
>>2**53
>>float(2**53) # is the same
>>float(2**53 + 1)  #not the same as 2**53 + 1

read:  what every computer scientist should know about
floating-point arithmetics


problem with floats they are converted to base 2 representation


decimal.Decimal type still a float but with base 10
Decimal should be used in Financial code for
any accounting calculations

>>>import decimal
>>> decimal.getcontext()
#shows defautl precison at 28

>>>from decimal import Decimal
Decimal stores numbers in base 10
>>Decimal(5)

>>Decimal('0.8')
>>> Decimal('0.8') - Decimal('0.7')
Decimal('0.1')
versus !
>>> Decimal(0.8) - Decimal(0.7)
Decimal('0.1000000000000000888178419700')
always specify arg as string
>>> decimal.getcontext().traps[decimal.FloatOperation]=True
>>> Decimal(0.8)  #will now raise excdeption
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]


>>> Decimal('Infinity')
>>> Decimal('-Infinity'
>>> Decimal('NaN')

>>> purchase = Decimal("20.44")
>>> current = Decimal("80.25")
>>> shares = 135
>>> shares * purchase
Decimal("2759.40")
>>> shares * current
Decimal("10833.75")
>>> shares*(current-purchase)
Decimal("8074.35")


Fraction type

complex type

abs()
round(0.2812,3)
round(1.5)
2
round(2.5)
2
##base conversions
bin() # base 2
oct() # base 8
hex() # base 16
int(x,base) # base 2 to 36


>>> 0b101010  #0b  base 2
42
>>> 0o52   # 0o base 8
42
>>> 0x2a   #0x base 16
42
>>> bin(42)
'0b101010'
>>> oct(42)
'0o52'
>>> hex(42)
'0x2a'
>>> int('42', base=10)
42
>>> int('2a', base=16)
42


(covers infinite calendar)
types datetime, date, time timedelta timezone
instances are immutable
! demo datetime-demo.py
    demo_datetime_date()
    demo_datetime_time()
    demo_datetime_datetime()
    demo_timedelta()
    demo_timezone()

! demo collinearity/textual/orientation.py

    shows how rounding errors in floats can affect geometric
    assumptions on collinearity

! demo collinearity/graphical/orientation.py
    change floats to Fractions -> get expected collinearity results

==============================
ch 08 iterables and iteration
==============================

review of comprehensions
    comprehesions with multiple sources
    values.py  values2.py
    nested comprehensions
        values3.py
iteration and iterables (functional style python)

map() applies a func to each element in a sequence
map() prduces lazy eval
i.e. it returns an iterator object

>>> m =map(lambda x:x*x, range(5))
>>>m
<map object at 0x10d380320>
>>> [x for x in m]

map acceps any number of input sequences. that number must match the number of function arguments
>>>m=map(pow, range(3),[2]*3)  #pow(x,y)
>>> [x for x in m]
[0, 1, 4]

filter() apply f to each element in an iterable series and skips those which don’t meet some criteria.
>>> positives = filter(lambda x: x>0, [1,-5,0,6,-2,8])
>>> [x for x in positives]
[1, 6, 8]
>>> trues = filter(None, [0,1,False,True,[],[1,2,3], '', 'hello'])
>>> [x for x in trues]
[1, True, [1, 2, 3], 'hello']

diff between python 2 and 3 
in python 2 map, reduce return lists not iterators

functools.reduce() #repeteadly apply a func to the elements of a  a sequence reducing  them to a single value
 
>>> def multipl(x,y):
...     print('mul {} {}'.format(x,y))
...     return x*y
>>> from functools import *
>>> reduce(multipl,range(1,10))
mul 1 2
mul 2 3
mul 6 4
mul 24 5
mul 120 6
mul 720 7
mul 5040 8
mul 40320 9
362880 # output  == 1*2*3*4*5*6*7*8*9

>>> reduce(multipl, [], 0)  # 0 - optional value returned by default if sequence is empty
0
! demo map_reduce.py
    canonical example to compbeing word doc counts
    from a list of documents
    map() apply count_words() to each doc
    reduce() combine those counts to a single dictionary


iteration protocols
iter()
next()
stopIteration
__iter__() #need to implement
iterator is an object which implements the iterable protocol

! demo example_iterator.py
implement simple iterator protocols


!demo alt_iterable.py

extended iter()
iter(callable, sentinel)  #common use = create infinite sequences from existing functions
extended iter()  with ending_file.txt 


! demo sensor.py
    infinite series by using iter()
    simulates data coming from a sensor  in  a stream


==========================================
ch 09 inheritance and subtype polymorphism
==========================================
!demo base.py

!demo sorted_list.py
    __init__ in inherited class does not automatically call
        it shoudl be specified explicitely !
    how derived are instantiated.
    how methods are resolved

!demo  sorted_list_demo.py

 sorted_list.py

 object
 |
 SimpleList -----|
 |               |
 SortedList    IntList
        |        |
       SortedIntList

    demo_sorted_list()
    demo_int_list()
    demo_multple_inheritance_list()
        show how method resolved with __mro__
    demo_diamond_mro_basic()
        show how method resolved with __mro__
    demo_super_sortedInstList()
        show how super

__mro__ is calculated with C3 algorithm:
    1. A C3 MRO ensures that subclasses come before their base-classes.
    2. C3 ensures that the base-class order as defined in a class definition is also preserved.
    3. C3 preserves the first two qualities independent of where in an inheritance graph you
       calculate the MRO. In other words, the MROs for all classes in a graph agree with respect to relative class order.


super()  #returns a super-proxy obj
bound and unbound proxies
bound in detail

sortedList explained !

object() as ultimate base class
dir(object) #to see all object attributes