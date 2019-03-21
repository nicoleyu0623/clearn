python fundamentals austin bingham

they have 3 courses
1. python fundamentals
2. python beyond the basics  7h  (closuers, numeric and scalar types, iterables)
3. advanced python    4h  (object internals,byte oriented programming, descriptors, instance create, metaclasses, class decorators, abstract base classes)

TC
######################## TC ###################
ch1 intro
ch2 getting started with python 2
ch3 strings  and collections
ch4 modularity   (! first demo project in pycharm )
ch5 objects
ch6 collections
ch7 handling exceptions
ch8 iterables
ch9 classes
ch10 files and ressource mgmt
ch11 shipping working and maintanable code
#############################################

######## DEMOS ###############

!! ex/me/ch4678/pyfund.py has many tests for many chapter from chap 6

demo  project ex/me/ch3/webparse/wparse.py
demo  project ex/me/ch4678/scrapwords/words.py

    tuple
        ex/me/ch4678/pyfund.test_ch6_collections_tuple()
    ## str
     !! ex/me/ch4678/pyfund.test_ch6_collections_str()
    partition
    format
    #range
    !! ex/me/ch4678/pyfund.test_ch6_collections_range()
    #list
    !! ex/me/ch4678/pyfund.test_ch6_collections_list
    #dict
    !! ex/me/ch4678/pyfund.test_ch6_collections_dict
    #set
    !! ex/me/ch4678/pyfund.test_ch6_collections_set
 

demo  project ex/me/ch4678/exceptional.py
    ex/me/ch4678/exceptional/test_ch7_except_conversion()
    ex/me/ch4678/exceptional/test_ch7_except_convert_return_error_code()
    ex/me/ch4678/exceptional/test_ch7_except_sqrt_heron()
    ex/me/ch4678/exceptional/test_ch7_except_sqrt_heron_value_error() 
    ex/me/ch4678/exceptional/test_ch7_except_api_exceptions()
    ex/me/ch4678/exceptional/test_ch7_except_api_makedir()
    ex/me/ch4678/exceptional/test_ch7_except_api_WinUnixGetkey()


    ex/me/ch4678/pyfund/test_ch8_iterables_comprehensions()
    ex/me/ch4678/pyfund/test_ch8_iterables_iter()
    ex/me/ch4678/pyfund/test_ch8_iterables_generators()
    ex/me/ch4678/pyfund/test_ch8_iterables_itertools()
    
    for chapter 9 on OOP
    ex/me/ch4678/pyfund/ooaitravel.py

    demo project ex/ch10/filehandle
    #for simple file reading, writing
    demo in proj ex/ch10/filehandle/files.main()

    demo ex/me/ch10/filehandle/recaman.main()
    demo ex/me/ch10/filehandle/series.main()  #reads a file created by recaman

    demo ex/me/ch10/filehandle/tryfractalbmp #calls fuctions from imagewriter module

    demo ex/me/ch10/filehandle/fridge.py

    demo ex/me/ch11/tdd_tanalyze/text_analyzer.py
##############################


NB! importing 
from pprint import pprint as pp
from  modulename import func_name, clas_name 
from  modulename import *


ch1 intro
	* web develpopment  prominent (django, flask, pyrami)
    * science   (astropy, biopython, numpy, scipy)
    * cloud ( ansible, boto3)
    * data science ( pandas, matplotlib, bokeh, tensorflow, scikit-learn)

    great ecosystem of packages open-source
    * python is expressive


	* book based on course he python apprentice,    the python journeyman, the python master

    * python is strongly typed (every variable has a defined type)
    * python is dynamically typed (no compilation precheck)

    * python is an interpreted language (byte compilation invisible)

    mutliple implementations of python
    c-python (most common), jython, RPython

    * python2 , python3 (feature)  important syntax differnces

    * powerful standard library (many functionalities available out of the box)

    python std lib  docs.python.org

ch2 getting started with python 2

  * course based on pyton 3.4 and later
  * install from python.org  on windows  or dmg for osx, on linux python3 included
  * in terminal  >python3  to start
   
  * in repl  _  means last result
  >>> 6*7
  42
  >>> _ -1
  41
  >>> print('hello, Python')  ## in python2 print does not require ()
  >Ctrl-D to exit  or exit() from repl  (Ctrl-Z on windows)
  indendation is singnificant (4 spaces)
  indentation starts after  a line finished with :  (eg loop body)
  eg.
  for i in range(5):
      	x = i * 10
      	print(x) 

  indentation = four spaces
  never mix spaces and tabs
  be consistent on consecutive lines
  => rigorous approach on code indentation ! 

  PEP (python ehancmen proposals) PEP 8, PEP 20
  >>> import this

  * python standard library (structured as modules)
   >>> import module_name
    ex
	>>> import math
	>>> math.sqrt(81)
	>>> 9.0
	>>> help(math)
	>>> help(math.factorial)
	>>> math.factorial(5)
	>>> 120
	>>> import math as mt
	>>> mt.factorial(5)
	>>> 120
	>>> mt.factorial(5) // 10  # for integer division
	>>>  3 // 2
	>>> 2**10
	1024
	## number of combinations
	>>> n = 100
	>>> k = 2
	>>> mt.factorial(n) // ( mt.factorial(k) * mt.factorial(n-k))
	4950  
	>>> len(str(mt.factorial(n)))
	158

   * scalar types and values 
	    int (arbitratry precision integer)
	    float  64-bit floating point numbers
	    None   the null object
	    True,False boolean logical values
    #### integers ######
    >>> 10
	10
	>>> 0b10  #binary
	2
	>>> 0o10  #octal
	8
	>>> 0x10  #hexadecimal
	16
	>>> int(3.5)
	3
	>>> int(-3.5)
	-3	
	>>> int("10000")
	10000
	##convert string to integers in base 2
	>>> int("1", 2)
	1
	>>> int("10", 2)
	2
	>>> int("100", 2)
	4
	 #### floats ######
    #>>> 3.125
	3.125
	>>> 3e8
	300000000.0
	>>> 1.616e-35
	1.616e-35
	>>> float("nan")
	nan
	>>> float("inf")
	inf
	>>> float("-inf")
	-inf
	#### None type #### 
	>>> a = None 
	>>> a is None 
	True
	>>> b = 1
	>>> b is None 
	False
	##### Boolean type ##### 
	False
	>>> bool(0)
	False
	>>> bool(1)
	True
	>>> bool(-1)
	True
	>>> bool(0.2)
	True
	>>> bool(None)
	False
	>>> bool([])
	False
	>>> bool([1,2])
	True

	#### relational operators ####
	 == , !=  <  >  <=  >=
	>>> g = 20
	>>> if g == 20:
	... 	print(g)
	... 
	20

   ### control flow statements 

   if expr: 
   		print("expr is true")

	>>> if bool("eggs"):
	... 	print("yes please")
	... 
	yes please
	>>> if "eggs":   ## explicit converstion to bool
	... 	print("yes please")
	... 
	yes please

    ##### if  elif  else  #######
	>>> h = 42
	>>> if h > 50:
	... 	print("greater than 50")
	... else:
	... 	print("50 or smaller")
	... 
	50 or smaller

    ##### while , for ######
	>>> x = 10
	>>> while x > 0:
	...     print(x)
	...     x-=1
  
    Ctrl-C to interrupt  looping

	>>> while True:
	...     print("enter integer input:")
	...     response = input()
	...     if int(response) % 7 == 0:
	...             break
	...
	enter integer input:
	10
	enter integer input:
	20
	enter integer input:
	7
	>>>

ch3 strings  and collections
	{str, bytes, list, dict}
	#### str  (immutable )
	str uses ''  or ""
	>>> "hello baby it's me"
	"hello baby it's me"
	>>> "first" "second"
	'firstsecond'
	>>> 
	>>> """ this is
	... a multiline
	... string"""
	' this is\na multiline\nstring'
	>>> m = "this string\nspans over\nfew lines"
	>>> print(m )
	this string
	spans over
	few lines
	>>> 

	#useful for windows paths
	>>> path = r'C:\Users\Merline\My Documents'
	>>> print(path)
	C:\Users\Merline\My Documents

	>>>help(str)
	>>> c = 'oslo'
	>>> c.capitalize()
	'Oslo'
	>>> c 
    ## default encoding is utf8
    >>> frs = "bonjour Jêrome, je suis enchanté"
	>>> print(frs)
	bonjour Jêrome, je suis enchanté
	>>> fru = "привет, придурки"
	>>> print(fru)
	привет, придурки
    >>>frs[0]
    >>>'b'

    ### bytes #### 
    immutable sequence of bytes

    ### bytes important in files, network resources, http responses
	>>> russian_input="тили тили трали вали"
	>>> data = russian_input.encode('utf-8')
	>>> print(data)
	b'\xd1\x82\xd0\xb8\xd0\xbb\xd0\xb8 \xd1\x82\xd0\xb8\xd0\xbb\xd0\xb8 \xd1\x82\xd1\x80\xd0\xb0\xd0\xbb\xd0\xb8 \xd0\xb2\xd0\xb0\xd0\xbb\xd0\xb8'
	>>> russian_output=data.decode('utf-8')
	>>> print(russian_output)
	тили тили трали вали

    ###lists #####
    mutable sequence of objects
	>>> li = [1,9,8]
	>>> ls = ['papa', 'mama']
	>>> li[0]
	1
	>>> ls[0]    
	'papa'
	>>> li[2] = 'son'  #mutability
	>>> li
	[1, 9, 'son']

	>>> b=[]  #empty list
	>>> b.append(1.618)
	>>> b.append(3.14)
	>>> b

	>>> list("characters")
	['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's'] 
	[1.618, 3.14]
	>>> c = ['bear',
	... 	'giraffe',
	... 	'elephant', ] ## additional comma ! (maintenability)
	>>> c 
	['bear', 'giraffe', 'elephant']
    
    ### dict  ####
    (mutable key-value mappings  key-value pairs)
    >>> d = {'alice': '878-000-111', 'bob': '256-123-456'}
	>>> d['alice']
	'878-000-111'
	>>> d['charles'] = '314-999-888' ## add new element
	>>> d
	{'alice': '878-000-111', 'bob': '256-123-456', 'charles': '314-999-888'} 

	#### for as for each ###
	>>> cities = ["london", "new york", "geneva", "moscow"]
	>>> for city in cities:
	...     print(city)
	...
	london
	new york
	geneva
	moscow

	>>> colors = {'crimpson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
	>>> for color in colors:
	...     print(color)
	...     print(color, colors[color])
	...
	crimpson
	crimpson 14423100
	coral
	coral 16744272
	teal
	teal 32896
 
    ### putting it together
    >>> from urllib.request import urlopen
    >>> with urlopen('http://sixty-north.com/c/t.txt')  as story:
    ...     story_words = []
    ...     for line in story:
    ...         line_words = line.decode('utf-8').split() #split line into words
    ...         for word in line_words:
    ...             story_words.append(word)
    ...
    >>> story_words
    ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 'the', 'season', 'of', 'Light', 'it', 'was', 'the', 'season', 'of', 'Darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the', 'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct', 'to', 'Heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']  

    !! demo  project ex/me/ch3/webparse/wparse.py



ch4 modularity
   
    associated functions form module
    module can use another module

    a module is a source file withh functions, classes

    !! demo  project ex/me/ch4678/scrapwords/words.py
    >cd  ex/me/ch4/scrapwords
    >python3
    >>>> import words
    >>> words.square(9)
    81
    >>> words.fetch_words()
    It
    was
    ....
    >>> from words import fetch_words
    >>>fetch_words()

    ## to make module run a specific function from cmd
    ## > python3  words
    if __name__ == '__main__':
        fetch_words()
    
    python module, python script  python program (composed of n modules)

    >>>import words
    >>>from words import (fetch_words, print_words)
    >>>print_words(fetch_words())

    >>> from words import *  ## explicit import is lost, opens to namespace clashes
    >>> square(10)
    100

    ##after param is set in main()
    >python3 words.py http://sixty-north.com/c/t.txt


    #modules for argument parsing:  argparse , docopt
    after adding docstrings  between """  """
    e.g.
    def fetch_words(url):
        """ Fetch a list fo words from a URl.
        Args:
         url:  the Url of a UTF-8 text document

        Returns:
            A list of string containing the words
            from the document
        """
    reimport the module, do help(func_name)
    >>> import words
    >>> from words import *
    >>> help(fetch_words)

    reimport the module and see the help on all module's functions
    >>> import words
    >>>help(words)

    add as module's first line (shebang)
    #!/usr/bin/env python3
    chmod+x  words.py
    and you can execute the module directly from the cmd line
    >words.py

ch5 objects
    >>> x=1000   # x is a reference points to the immutable integer object 1000
    >>>x=500    # x reference is pointed to another object 500, 1000 will be gc_ed
    >>>y=x      # second reference is pointing to the same object
    >>> a=496
    >>> id(a)  # used for debugging
    4306931536
    >>> b=a
    >>> id(b)
    4306931536    
    >>> id(a)==id(b)
    True
    >>> a is b  # more commontly used
    True 
    >>> a is None
    False     
    
    >>> t=5
    >>> id(t)
    4303181776
    >>> t+=2
    >>> id(t)
    4303181840   # t reference points to another immutable int object different memory address
    #!this works for all python types.   assignment operator = references,  no copies by val

    >> r=[1,2,3]
    >>> s=r # reference to the same memory adress
    >>> s.append(4)
    >>> r
   [1, 2, 3, 4]
    >>> r is s
    True
  
    !!! variables are  named references to objects !!!

    >> p = [4,7,11]
    >>> q = [4,7,11]
    >>> p == q
    True
    >>> p is q
    False
    >>> id(p)
    4307326024
    >>> id(q)
    4307326088

    value equal  == contents is equal
    identity equal - same object (same memory address)
 
    ##func argument is passed by reference !
    >>> m = [9,15,24]
    >>> def modify(k):  #k second reference to the same list object as m
    ...     k.append(39)
    ...     print("k =", k)
    ...
    >>> modify(m)
    k = [9, 15, 24, 39]
    >>> m
    [9, 15, 24, 39]


    >>> f = [1,2,3]
    >>> def replace(g):
    ...     g = [11,12,13]
    ...     print("g =", g)
    ...
    >>> replace(f)    # here arg g would point to the same [1,2,3] as f
    g = [11, 12, 13]  #here g gets reassigned to another object
    >>> f             #f points to the older object so it is unchanged
    [1, 2, 3] 

    >>> def replace_bis(g):
            g[0] = 17
            g[1] = 28
            g[2] = 45
         print("g =", g)

    >>> replace_bis(f)  # this time f contents will be replaced
       

    >>> def argv(c):
    ...     return(c)
    >>>f = [1,2,3]  
    >>> g = argv(f)
    >>> g is f
    True          ##this means no copying of argument happened

    ## function args with default value
    >>> def banner(message, border='-'):
    ...     line = border * len(message)
    ...     print(line)
    ...     print(message)
    ...     print(line)
    ...
    >>> banner("hello world")
    -----------
    hello world
    -----------
    >>> banner("hello world", border="*")
    ***********
    hello world
    ***********

    ## the default arg value evaluates only once when package is imported
    def showtime(arg=time.ctime()):
        print(arg)

    >>> def add_spam(menu=[]):
    ...     menu.append("spam")
    ...     return menu
    ...
    >>> l = []
    >>> l = add_spam()
    >>> l
    ['spam']
    >>> l = add_spam()  ## calling for 2nd tme with default empty arg, the
    >>> l               ## the arg is actually not empty
    ['spam', 'spam'] 
    ### solution
    >>> def add_spam(menu=None):
    ...     if menu is None:
    ...         menu = []
    ...     menu.append('spam')
    ...     return menu
    >>> l = []
    >>> l = add_spam()
    >>> l
    ['spam']
    >>> l = add_spam()
    >>> l
    ['spam']

     # python strong dynamically typed
    >>> def add(a,b):
    ...     return a + b
    ...
    >>> add(5,7)
    12
    >>> add(3.1, 3)
    6.1
    >>> add('news','paper')
    'newspaper'
    >>> add([1,2], [5,6])
    [1, 2, 5, 6]
    >>> add('answer is', 42)         ## fails to implicitly convert
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in add

    ### object references have no type !  ## 
    
    python names scopes
    L ocal      names in function
    E nclosing  names inside inclosing function
    G lobal     module wide names e.g. func names in module or imported modules
    B uilt-in

    check global  keyword  to access a global variable scope (occasionaly)

    ## in python everything is an object !! # 
    >>import words
    >>type(words)
    >> dir(words)
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fetch_words', 'is_even', 'main', 'print_items', 'square', 'sys', 'urlopen']

    >>> dir(words)
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fetch_words', 'is_even', 'main', 'print_items', 'square', 'sys', 'urlopen']
    >>> dir(words.fetch_words)
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    >>>

    >>> words.fetch_words.__doc__
    ' Fetch a list fo words from a URl.\n    Args:\n     url:  the Url of a UTF-8 text document\n\n    Returns:\n        A list of string containing the words\n        from the document\n    '
    

    >>> type(words.fetch_words)
    <class 'function'>

ch6 collections

    tuple, str, list, dict, 

    tuple: ('a', 1, 1.2323)
    list: [a,b,c]
    dict: {k1:v1, k2:v2}
    set: {a,b,c}

    tuple
    demo !! pyfund.test_ch6_collections_tuple()
    ## str
     !! pyfund.test_ch6_collections_str()
    partition
    format
    #range
    !! pyfund.test_ch6_collections_range()
    #list
    !! pyfund.test_ch6_collections_list
    #dict
    !! pyfund.test_ch6_collections_dict
    #set
    !! pyfund.test_ch6_collections_set

    collection PROTOCOLS
        Container:          str, list, range, tuple, bytes, set, dict
        Sized (len):        str, list, range, tuple, bytes, set, dict
        iterable:           str, list, range, tuple, bytes, set, dict
        Sequence: ([])      str, list, range, tuple, bytes
        Mutable Sequence:   list 
        Mutable Set:        set
        Mutable mapping:    dict


ch7 handling exceptions

    !! demo exceptional.main()

    exceptions can be seen as breakdowns from light to critical
    exceptions are commonly raised in python   

   
   use system defined exceptions
   rarely define your own exception

   IndexError
   KeyError
   ValueError
   TypeError
   etc...

   ! do not check for error types inside functions. 
   ! use try except blocks in the calling code

   dealing with exceptions  2 philosophies

   Look before you leap  LBYL
   It's Easier to Ask fo Forgiveness than  Permission  EAFP
   python adheres more  to EAFP 

   === LBYL approach:
   import os
   p = '/path/to/datafile.dat'
   if os.path.exists(p):   
       process_file(p)
   else:
        print('no such file as{}'.format(p))

   === EAFP approach:
   import os
   p = '/path/to/datafile.dat'
   try:
        process_file(p)
    except OSError as e:
        print('Could not process file because {}'.format(str(e)))


    ex/me/ch4678/exceptional/test_ch7_except_conversion()
    ex/me/ch4678/exceptional/test_ch7_except_convert_return_error_code()
    ex/me/ch4678/exceptional/test_ch7_except_sqrt_heron()
    ex/me/ch4678/exceptional/test_ch7_except_sqrt_heron_value_error() 
    ex/me/ch4678/exceptional/test_ch7_except_api_exceptions()
    ex/me/ch4678/exceptional/test_ch7_except_api_makedir()
    ex/me/ch4678/exceptional/test_ch7_except_api_WinUnixGetkey()



ch8 iterables

    comprehensions
        concise syntax to describe a list , set or dict
    >>>t=['mama', 'papa', 'syn']
    >>>tl = [len(word) for word in t]

    generators a lazily evaluated!!
    

    ex/me/ch4678/pyfund/test_ch8_iterables_comprehensions()
    ex/me/ch4678/pyfund/test_ch8_iterables_iter()
    ex/me/ch4678/pyfund/test_ch8_iterables_generators()
    ex/me/ch4678/pyfund/test_ch8_iterables_itertools()


ch9 classes
    

    demo project ex/me/ch4678/pyfund/ooaitravel.py
    demo runner ex/me/ch4678/pyfund/ooaitravelrunner.py

    retest in repl a func after a change
    >>> import importlib
    >>> importlib.reload(ooairtravel)
    >>> from ooairtravel import make_flights
    >>> f,g = make_flights()  #will see new changes 



    class Flight:

        def __init__(self, number):   #__init__() is an initializer, not the constructor
            self._number = number     # nameing _number for instance variables

        def number(self):
            return self._number

    >>>from airtravel import Flight
    f = Flight("SW111")
    f.number()
    Flight.number(f) #also works

    python all methods are public

    f._number  works two but people tend not to use it in prod code

    class invariants
    eg. flight number starts with two Capital chars followed by 3 or 4 digits

    put them in the initializer
    once class invariants have been established, most methods are usually simple 

    add-hoc testing in the repl is a very effective technique during development

    Law of Demeter :  the principle of least knowledge
        You should never call methods on objects you receive from other calls
        E.G.  only talk to your friends

    f = Flight("SW111", Aircraft("SB-101", "Airbus-320", num_rows=30, num_seats_per_row=6))

    new req. boarding card printer
    OO with function objects
    
    def console_card_printer is a module function
    used as an arg in Flight class method make_boarding_cards()
        this is an example of polymorphism

    inheritance
        python uses late binding
        python inheritances uses loose coupling

    ACL  there are no public, protected or private access modifiers i python    


ch10 files and ressource mgmt
    !! demo project filehandle
    # for simple file reading, writing
    !! demo in proj filehandle files.main()

    !demo ex/me/ch10/filehandle/recaman.main()
    !demo ex/me/ch10/filehandle/series.main()  #reads a file created by recaman   
    !demo ex/me/ch10/filehandle/tryfractalbmp.main 

    open(file, mode, encoding)
        python distinguishes open file in binary mode and text mode
    write()
    read()
    >>>import sys 
    >>>sys.getdefaultencoding()
    'utf-8'
     
     mode: 
        r  open for reading
        w open for writing truncating the file first
        x open for exclusive creation, fails if file exists
        a  open for writing at the end of file, (append)
        b binary bode
        t text mode (default)
        + open a disk file for updating (reading and writing)
        U  universal newlines mode (for backwards compatibiliy)

     * using with blocks   
       !! demo  ex/me/ch10/filehandle/recaman.main()

       working with files using with-blocks
       !! demo ex/me/ch10/filehandle/series.main()  #reads a file created by recaman

    writing reading binary files,  bmp example
    !demo tryfractalbmp.main  which imprts  bmp.py and fractal.py

    files as iterators 
    ! demo  emo in proj filehandle files 
        file_like_iterator()
        url_response_like_iterator()

    * closing with context managers
    ! demo fridge.py

        check how fridge closes after the exception with fried pizza was raised!

ch11 shipping working and maintanable code
    * unittest  module
        unit tests
        integration tests
        acceptancde tests

        TestCase
        Fixture  setUp() and tearDown() runs before after each test
        assertions
        acceptance tests

    !! demo project tdd_tanalyze  text_analyzer.py

       spec  for a function which opens a file
       and analyzes its contents
        NB start from writing the test
        before writing the business function

    * the PDB  debugger
    >>> import pdb
    >>> pdb.set_trace()
    >>>help

    >python3 -m pdb palindrome.py
    (pdb) where   # shows the current line
    (pdb) next
    (pdb) cont
    if in infinite loop
    (pdb) Ctrl-C
    (pdb) list

    * virtual environments
         ligt-weight self contained  python installation
    
    python -m venv
    ## do not need system admin rights

    #### create a virtual env named venv3
    >/usr/local/bin/python3 -m venv venv3
    ##activate it
    >source venv3/bin/activate  #this makes python3 from the venv3 install

    in a project dir create setup.py

    setup.py  has setup() function

    ! demo ex/me/ven3

    in the same project folder, create a venv dir
    >/usr/local/bin/python3 -m venv palindrom_env
    >source palindrom_env/bin/activate
    >python setup.py install
    ## this copies palindrome.py into the venv/lib/python3/site-packages
    >cd ..
    >python
    >>>import palindrome
    >>>palindrome.__file__  #shows the path to the package file

    * packaging with sdist

    from the project source folder
    >python setup.py sdist --format zip
    >ls dist
    apple$ unzip -l dist/palindrome-1.0.zip
    Archive:  dist/palindrome-1.0.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
         1433  04-04-2018 17:13   palindrome-1.0/palindrome.py
          262  04-04-2018 17:45   palindrome-1.0/PKG-INFO
          318  04-04-2018 17:33   palindrome-1.0/setup.py
    ---------                     -------  

   >python setup.py sdist --help-formats
   >python setup.py --help


   !demo  me/making_pkg  # python-apprentice: Appendix B


   * installing packages
   pip is an official  core lang tool

   anaconda is a bundle for numpy scipy  use

   doc: python packaging user guide

   PyPI  python package index 

   https://pypi.python.org/pypi

   installing nose with pip
   venv3> pip install nose
   >cd ../../palindrom
   > nosetests palindrome.py
   >cd dist
   >pip install palindrome-1.0.zip  #installs palindrome into venv3
   >pip uninstall palindrome-1.0.zip


