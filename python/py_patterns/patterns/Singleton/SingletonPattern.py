


class OnlyOne:
    """delegate object creation to a private nested class"""
    class __OnlyOne:    #naming strting with __ user cannot access
        def __init__(self,arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

        def getValue(self):
            return self.val

        def setNumAttribute(self, value):
            self.numval = value

        def getNumAttribute(self):
            return self.numval


    instance = None

    def __init__(self,arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self,name):    #this method redirecots to calls in inner class
        return getattr(self.instance,name)  #i.e getValue(), setNumAttribute()



if __name__ == '__main__':

    x = OnlyOne('sausage')
    print(x)
    print(x.getValue())
    x.setNumAttribute(10.0)
    print(x.getNumAttribute())
    y = OnlyOne('eggs')
    print(y)
    print(y.getValue())
    print(y.getNumAttribute())

