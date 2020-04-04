
# variable

answer = 42

answer = "the answer is 42"

#data types (boolean, int, double, char, string, list, dictionary, tuple, null

i = 3
f = 1.23
string ="strings are fun"
lst = ["el1", "el2", "el3"]
tpl = ("aa", 2)
dict = {"one":1, "two":2}
var_null = None

#cond
if i == 1:
    print("i is one")
elif i == 2:
    print("i is two")
else:
    print("i is neither 1 or 2")


for i in range(len(lst)):
    print(lst[i])

for item in lst:
    print(item)

#funcs
def summ(par1,par2):
    s = par1+par2
    return s

print("test summ on 1,2:",summ(1,2))

#classes
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age +=1

    def obj2str(self):
        print("Person named: {0} with age: {1}".format(self.name, self.age))

p1 = Person("John",32)
p1.birthday()
p1.obj2str()
