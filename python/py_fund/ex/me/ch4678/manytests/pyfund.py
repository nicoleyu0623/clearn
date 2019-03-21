#!/usr/bin/env python3
"""Test python language features

Usage:
    python3 pyfund.py

"""


def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def starprint(message,stars=2):
        mstars = '*' * stars
        ending = ''
        if stars == 4:
                ending = '!'
        newline = ''
        if stars == 2:
                newline='\n'
        print(newline,mstars,message,ending)


def test_ch6_collections_tuple():
    banner("test_ch6_collections_tuple")
    starprint('tuple is a heterogeneous immutable sequence')
    tpl = ("norway", 3.14, 3)
    print(tpl)
    print("tpl length:", len(tpl))
    print("2nd tpl element", tpl[1])
    print("iterate over tpl")
    for item in tpl:
            print(item)
    starprint("we can add elements to tpl. tpl is immutable")
    tpl = tpl + (3.1423123, 2.5e-10)
    print(tpl)
    starprint('nested tuples')
    a = ( (220,284), (1184, 1210), (2620,294))
    print(a)
    print('accssing a nested element; individual value', a[2], a[2][1] )
    print('create a single element tuple k=(391,):')
    k = (391,1)
    print(type(k))
    print('empty tuple')
    e = ()

    starprint('tuple unpacking')

    def minmax(items):
            return min(items), max(items)

    mimx = minmax([83,33,32, 101, 9]) #returns a tuple
    lower, upper = minmax([83,33,32, 101, 9]) #unpacks tuple into two vars
    print('unpacked tuple for min and max:',lower, upper)
    starprint('tuple unpacking works with arbitrarily nested tuples')
    (a, (b, (c,d))) = (4,(3, (2,1)))
    print(a)
    print(b)
    print(c)
    print(d)
    starprint('idiom to swap two or more variables')
    a = 'jelly'
    b = 'bean'
    a, b = b, a
    print(a)
    print(b)

    starprint("use tuple constructor to create tuple from other collections")
    print(tuple([2323,341,33,22]))
    print(tuple("Carand'ache"))
    print('in or not in operator with tuples: container protocol')
    print(5 in (3,4,8,5))
    print(4 not in (3,4,8))


def test_ch6_collections_str():
    banner(message='test_ch6_collections_str')
    starprint('str is homogenious immutable sequence of unicode codepoints ')
    print('length of mama str:', len('mama'))

    starprint('inefficient way of concatenating strings with +')
    s = "New"
    s += "found"
    s += "land"
    print(s)
    print('efficient joining with join()')
    island = ''.join(['New', 'found', 'land'])
    print(island)
    colors = ';'.join(['#11111', '#222222', '#333333'])
    print(colors)
    print('splitting with split():', colors.split(';'))

    starprint("partition()")
    print('see how unforgetable divided', "unforgetable".partition("forget"))
    departure, separator, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)

    starprint('if not interested in separator value use a _ variable which is dummy by convention', 1)
    origin, _, destination = "Seattle:Boston".partition(':')
    print(origin, destination)

    starprint('format(). use it to insert values into strings')
    print("The age of {0} is {1}. Hase he/she children: {2}".format('Jim', 32, True))
    print("Reticulating splin {} of {}.".format(4,23)) # we can avoid indexing inside {}
    print("Current position {latitude} {longitude}". format(latitude="60N",  #statement on multi-lines
                                                            longitude="5E"))
    print('using indexes in format()')
    pos = (65.2, 23.1, 82.2)
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=pos) )

    print('using object attributes in format()')
    import math
    print( "Math constants: pi={m.pi}, e={m.e}".format(m=math) )
    print( "Nice format Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math) )

    starprint("for help hit help(str)")

def test_ch6_collections_range():
    banner('test_ch6_collections_range')

    print('range() can be called with only 1 end arg range(5)')
    print(list(range(5)))
    for i in range(5):
            print(i)
    print('range() can be called with start, stop, step args')
    print(list(range(5,10)))
    print(list(range(0,10,2)))

    starprint('poor coding style using range')
    s = [0,9,11,13]
    for i in range(len(s)):  #works but poor style
            print(s[i])
    starprint('for collections looping always use the iteration approach')
    for v in s:
            print(v)

    starprint('prefer enumerate() for counters, which produces a tuple')
    t = [6,9,21,121312]
    for i,v in enumerate(t):
            print("i={}, v={}".format(i,v))

    starprint('because of strong iteration primitives in python range() is not widely used',stars=3)



def test_ch6_collections_list():
    banner('test_ch6_collections_list')

    s = "show how to index into sequences".split()
    print('string after a split is a list', s)
    print('access by index 2nd element of s:',s[1])

    starprint("accessing elements from the end")
    print('last nth element and n-1 element:', s[-1], s[-2] )

    starprint('accessing a subrange of a list')
    print(s[1:4])
    print('all elements between first and last not included', s[1:-1])
    print('from 3rd to end of list', s[3:])
    print('from start to 4th, not inluding the 4th', s[:4])

    starprint(' vec = existing_vec[:] creates a distinct copy of  vec')
    print('full_slice = s[:]')
    full_slice = s[:] #assignment
    print('full_slice is s:', full_slice is s)
    print('full_slice == s:', full_slice == s)
    full_slice[0] = 'MODIFIED'
    print(full_slice)
    print(s)

    starprint('more obvious methods of copying the list vec.copy(), list(vec)')
    u = s.copy()
    print(u is s , u == s )
    v = list(s)
    print(v is s , v == s )

    starprint('all these methods create shallow copies', stars=4)
    print('a shallow copy is a new list containing the same object references as the source list')

    print('lets see the example of this,  element reassignment, element modification')
    a = [ [1,2], [3,4]]
    b = a[:]
    print('a is b:', a is b)
    print('a[0] is b[0]:', a[0] is b[0])
    a[0] = [8,9]
    print('after assignment of the first  element of a')
    print('a[0] = [8,9]')
    print('a', a)
    print('b', b)
    print('after modification of the 2nd  element of a see how b is changed')
    a[1].append(5) # we modify the existing list without reassigning it
    print('a[1].append(5)')
    print('a', a)
    print('b', b)

    starprint('list repetition with * operator')
    x = [0] * 10
    print(x)
    print('list repetition is shallow')
    nx = [[-1,1]] * 5
    print(nx)
    nx[2].append(0)  # modifying an inner list referenced from all index positions
    print(nx)

    starprint('finding an element in the list with .index()')
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    i = w.index('fox')
    print('fox element:', w[i])
    print("counting the same elements  w.count('the'):", w.count('the'))

    starprint('container protocol for lits in , not in')
    print('37 in [1,2,37]:',37 in [1,2,37])
    print('5 not in [1,2,37]:', 5 not in [1, 2, 37] )

    starprint('append remove from list')
    x = [1,2,3,4]
    print(x)
    x.append(5)
    print('after x.append(5)',x)
    del x[2]
    print('after del x[2]', x)
    x.remove(5)
    print('after x.remove(5)', x)
    print('this is equivalent to  del x[x.index(5)]')

    starprint('inserting element at a given index ')
    a = "I accidentaly the whole universe".split()
    a.insert (2, "destroyed")
    print('a after a.insert (2, "destroyed")', a)

    starprint('assembling a string from a list of str elements with .join()')
    s = ' '.join(a)
    print("after s = ' '.join(a)", ' '.join(a))

    starprint("make list grow with +, +=, extend() ")
    m = [2,1,3]
    n = [4,7,11]
    k = m + n
    print("k = [2,1,3] + [4,7,11]", k)
    k += [18,29]
    print("k += [18,29]", k)
    k.extend([76,111,221])
    print("k.extend([76,111,221])", k)

    starprint("sorting and reversing  lists")
    g = [1,11,21, 1211, 122222]
    print("g",g)
    g.reverse()
    print("g.reverse()",g)
    d = [1,4,-3, 9, -121, 18,13]
    print("d",d)
    d.sort(reverse=True)
    print("in-place sorting: d after d.sort(reverse=True", d)
    print("sort with key as a func for sorting")
    h = 'not perplexing do handwritin family where i illegibly know doctors'.split()
    print(h)
    h.sort(key=len)
    print("h after h.sort(key=len)  ' '.join(h) ", ' '.join(h) )

    print("* sorting , reversing with assignment")
    x = [4,9,2,1]
    y = sorted(x)
    print("x, y = sorted(x), y is x:", x,y, y is x)
    z = reversed(y)
    print("z = reversed(y), list(z)", list(z))


def test_ch6_collections_dict():
    banner("test_ch6_collections_dict")
    print('dict is an unordered mapping from unique, immutable keys to mutable values')
    print('eg  lists as keys can not be used')
    urls = { 'google': 'http://google.com',
             'pluralsight': 'http://pluralsight.com',
             'microsoft': 'http://microsoft.com' ,}
    print(urls)
    print("* with pretty printing")
    from pprint import pprint as pp
    pp(urls)
    print("\nurls['pluralsight']:", urls['pluralsight'])

    starprint("dict constructor")
    names_and_ages = [ ('Alice', 32), ('bob', 41), ('Charly', 28), ('Kira', 15), ('John', 68) ]
    print("list of key-value tuples",names_and_ages)
    d = dict(names_and_ages)
    print("converted to dictionary")
    pp(d)

    print('look how a=, b= transformed into dictionary keys')
    phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='elena', f='foxtrot',
                    g='geneva')
    pp(phonetic)

    starprint("copying dictionaries  d.copy() or dict(d)")
    e = phonetic.copy()
    print('e = phonetic.copy():')
    pp(e)
    f = dict(phonetic)
    print("f = dict(phonetic)")
    pp(f)

    starprint("extend a dictionary with update()")
    newchars = dict(h='halo', i='input', j='jumbo')
    print('newchars')
    pp(newchars)
    f.update(newchars)
    print('after f.update(newchars)')
    pp(f)
    print('update updates values for existing keys' )
    stocks = {'GOOG': 891, 'MSFT': 112, 'YHOO': 55}
    pp(stocks)
    stocks.update( {'GOOG': 894, 'MSFT': 117})
    print("stocks.update( {'GOOG': 894, 'MSFT': 117})")
    pp(stocks)

    starprint("dicts are iterable but order is unpredicted")
    for key in stocks:
            print("{key} => {value}".format(key=key, value=stocks[key]))

    print("dict can iterate over values")
    for value in stocks.values():
            print(value)

    print("dict can iterate over key,value using  .items()")
    for key, value in stocks.items():
            print("ticker {key} => price {value}".format(key=key,value=value) )


    starprint("container protocol for dict (in not in")
    symbols = dict(usd='\u0024', gbp='\u00a3', jpy='\u00a5')
    print("currency symbols:")
    pp(symbols)
    print("'usd' in symbols :", 'usd' in symbols)
    print("'nzd' in symbols:",'nzd' in symbols)


    starprint("deleting element from dict")
    del symbols['jpy']
    print("symbols after del symbols['jpy']")
    pp(symbols)


    starprint("add new element to dict")
    symbols['eur'] = '\u20ac'
    print("symbols after adding eur")
    pp(symbols)

def test_ch6_collections_set():
    banner("test_ch6_collections_set")
    print("a set is an unordered collection of unique, immutable objects")
    p = { 6, 28, 496, 818}
    print(p)
    print(type(p))

    starprint("set is a good way to get rid of duplicates in a list. set() constructor")
    s = set([ 4,5, 6, 1, 9,6, 4 ])
    print(s)
    print("list(s) after s = set([ 4,5, 6, 1, 9,6, 4 ]):", list(s))

    starprint("add remove items from set")
    k= {81, 108}
    print("defined k:",k)
    k.add(54)
    print("after k.add(54):",k)
    k.remove(81)
    print("after k.remove(81):", k)
    k.discard(54)
    print("after k.discard(54):", k)

    starprint("copying set")
    j = s.copy()
    print("after j = s.copy():",j, "identity of j, s:", j is s)

    starprint("set algebra !")
    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
    blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}

    b_bood   = {'Amelia', 'Jack'}
    a_blood  = {'Harry'}

    print('set union: (A + B) blue_eyes.union(blond_hair):',blue_eyes.union(blond_hair))
    print('commutativity:',blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)  )
    print('set intersection  (A and B) blue_eyes.intersection(blond_hair):', blue_eyes.intersection(blond_hair))
    print('set difference A - B blond_hair.difference(blue_eyes):', blond_hair.difference(blue_eyes))
    print('set complement of intersection !(A and B) blond_hair.symmetric_difference(blue_eyes): ', blond_hair.symmetric_difference(blue_eyes))

    print('A is subset of B smell_hcn.issubset(blond_hair)', smell_hcn.issubset(blond_hair))
    print('A is superset of B taste_ptc.issubset(smell_hcn):', taste_ptc.issubset(smell_hcn))
    print(' A and B disjoint a_blood.isdisjoint(b_bood):', a_blood.isdisjoint(b_bood))


def is_prime(x):
    """ return True if the argument is a prime number"""
    from math import sqrt
    if x < 2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True



def test_ch8_iterables_comprehensions():
    banner("comprehensions")
    words = "why sometimes I have beleived as many as six impossible things before breakfast".split()
    print(words)
    print("apply len() to each element in a list and put the result in the list")
    words_length = [ len(word) for word in words ]  #comrehension 1 liner
    print("words length:", words_length)

    from math import factorial
    factorials = [factorial(x) for x in range(15)]
    print("factorials:",factorials)
    fl = [len(str(factorial(x))) for x in range(15)]
    print('number lengths of 15 first factorials')
    print(fl)

    starprint("comhrehensions work on sets as well")
    sf = {len(str(factorial(x))) for x in range(15)}
    print(sf)  #only unique elements
    print(type(sf))

    starprint("dictionary comhrehensions")
    from pprint import pprint as pp
    country_to_capital = {'United Kingdom': 'London', 'Switzerland': 'Bern', 'Russia': 'Moscow', 'Sweden':'Stockholm',}
    pp(country_to_capital)

    capital_to_country = {v: k for k,v in country_to_capital.items() }  #comprehension
    print('*key value swapped')
    pp(capital_to_country)

    print('* duplicate keys are overwriten')
    words = ["hi", "hello", "foxtrot", "hotel" ]
    print(words)
    fc = { x[0]: x for x in words}
    pp(fc)

    starprint("example use comprehension for globbing")
    import os
    import glob
    file_sizes = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*.py')}
    pp(file_sizes)

    starprint("comprehension with filtering")
    from math import sqrt
    first_primes = [ x for x in range(31) if is_prime(x)] # only if it is a prime number, save it to the list
    print('primes in first 31 numbers:', first_primes)


    prime_square_divisors = { x*x: (1,x, x*x) for x in range(31) if is_prime(x)}
    print('numbers with only 3 divisors from the first 31 numbers')
    pp(prime_square_divisors)


def test_ch8_iterables_iter():
    banner("iter() on iterables")

    iterable = ['a', 'b', 'c']
    print(iterable)
    iterator = iter(iterable)
    v = next(iterator)
    print(v)
    v = next(iterator)
    print(v)
    v = next(iterator)
    print(v)
    #v = next(iterator) # out of index  raises StopIteration exception


    def first(iterable):
        iterator = iter(iterable)
        try:
            return next(iterator)
        except StopIteration:
            raise ValueError("iterable is empty")

    print(first(['1st', '2nd']))
    #print(first([])) # on empty vec expect an exception raise

def test_ch8_iterables_generators():
    banner("generators  yield keyword")
    def gen123():
        yield 1
        yield 2
        yield 3

    g = gen123()
    print(type(g))
    v = next(g)
    print("v = next(g):",v)
    v = next(g)
    print("v = next(g):",v)
    v = next(g)
    print("v = next(g):",v)
    #v = next(g) # out found raises  StopIteration exception
    for v in gen123():
        print(v)

    starprint("stateful generators. lazy evaluation ")

    def take(count, iterable):    #generator 1
        """Take items from the front of an iterable
        Args:
           count: The maximum number of items to retrieve.
           iterable: The source of the items.
       Yields:
           At most 'count' items from 'iterable'.
        """
        counter = 0
        for item in iterable:
            if counter == count:
                return
            counter += 1
            yield item

    def distinct(iterable):    #generator 2
        """Return unique items from the iterable argument
            Args:
                iterable: The source of the items.
            Yields:
                Unique elements in order from 'iterable'.
        """
        seen = set()
        for item in iterable:
            if item in seen:
                continue
            yield item
            seen.add(item)


    print('testing generator take() on list [11,12,13,14,15] ')
    print(list(take(3, [11,12,13,14,15])))
    print('testing generator distinct() on list [11,11,12,13,14,15,11,12]')
    print(list(distinct([11,11,12,13,14,15,11,12])))

    def run_pipeline(count,iterable):
        for item in take(count, distinct(iterable)):  # ! combine take() and distinct()
            print(item)

    print('testing a pipeline with 5 elems from [1,1,1,1,1,4,4,4,4,3,2,2,3,3,3,9,9,8,11,11]')
    run_pipeline(5, [1,1,1,1,1,4,4,4,4,3,2,2,3,3,3,9,9,8,11,11])

    starprint("generators are lazy")
    million_squares = (x*x for x in range(1,1000001))
    print("as of now not much memory has been allocated")
    print(type(million_squares))
    #print(list(million_squares)) #only at this moment a 40 megs of ram are allocated

    print('not much memory is allocated when using operators on generators')
    print('sum of squares of first 1 miillon numbers:',sum(million_squares))


    def lucas():
        """a generator for a infinite serie"""
        yield 2
        a = 2
        b = 1
        while True:
            yield b
            a,b = b, a + b

    print("testing lucas serie generator untill 10000")
    for x in lucas():
            if x > 10000:
                break
            print(x)

def test_ch8_iterables_itertools():
    banner("itertools module")
    from itertools import islice, count
    thousand_primes = islice((x for x in count() if is_prime(x)),1000)
    print('create first 1 thousand of prime numbers')
    print(type(thousand_primes))
    print("sum of first thousand primes:",sum(islice((x for x in count() if is_prime(x)),1000)))
    print("list of first 1000 primes", list(thousand_primes))

    starprint("any, all in standard library")
    print("any:", any([False,False,True]))
    print("all:", all([False,False,True]))

    print('chk if there are any primers in the range:',any(is_prime(x) for x in range(1328, 1361)))

    print('chk that al elements start with uppercasec char',
          all(name == name.title() for name in ['London','New York', 'Sydney']))

    starprint("merging sequences with zip")
    sunday_temp = [12, 14, 15, 15]
    monday_temp = [13, 14, 14, 14]
    tuesday_temp = [11, 12, 11, 10]

    for item in zip(sunday_temp,monday_temp):
            print(item)
    starprint("pretty printing with some avg operation",1)
    for sun, mon in zip(sunday_temp, monday_temp):  #like binding lists
            print("sunday: {}, monday: {}, row average {}".format(sun,mon, (sun+mon)/2))

    starprint('zipped sequence with min max average operators applied',1)
    for temps in zip(sunday_temp, monday_temp, tuesday_temp):
        print("per row: min={:4.1f}, max={:4.1f}, average{:4.1f}"
              .format(min(temps), max(temps), sum(temps)/len(temps)))


def test_ch10_files_basic_read_write():
    banner("test_ch10_files_basic_read_write")

    starprint("writing")
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    f.write('What are the roots that clutch,')
    f.write('What branches grow.\n')
    f.write('Out of this stony rubbish?\n')
    f.write('I am out of this situation.')
    f.close()
    print("* check the file written by calling a sys call to cat")
    from subprocess import call
    call(["cat", "wasteland.txt"])

    starprint("reading")
    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    print(g.read(31))  # read a specified number of chars from the beginning
    print(g.read(20))  # read next 19 chars
    print(g.read())  # read from that file pointer position till the end
    print(g.read())  # returns empty str  as the file pointer is already at the file's end
    g.seek(0) # rewind the file pointer to the file's start
    print("we can rewind to start by g.seek(0)")

    starprint("reading by line")
    print(g.readline())

    g.seek(0)
    lines = g.readlines()  # all lines in a list
    print(len(lines))
    g.close()

    #append

def main():
    """ Run tests python language features
    """
    #test_ch6_collections_tuple()
    #test_ch6_collections_str()
    #test_ch6_collections_range()
    #test_ch6_collections_list()
    #test_ch6_collections_dict()
    #test_ch6_collections_set()
    #test_ch8_iterables_comprehensions()
    #test_ch8_iterables_iter()
    test_ch8_iterables_generators()
    #test_ch8_iterables_itertools()

    #test_ch10_files_basic_read_write()

if __name__ == '__main__':
    main()
