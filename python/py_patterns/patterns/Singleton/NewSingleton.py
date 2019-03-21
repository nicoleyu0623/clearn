

class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            #return 'self:' + self.val
            return repr(self) + self.val

    instance = None  #a class attribute

    def __new__(cls): #__new__ always a class method
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance

    def __getattr__(self,name):
        return getattr(self.instance,name)  #delegating to inner class
    def __setattr__(self,name):
        return setattr(self.instance,name)

if __name__ == '__main__':

    x = OnlyOne()
    x.val = 'sausage'
    print(x)
    y = OnlyOne()
    y.val='eggs'
    print(y)
    z=OnlyOne()
    z.val='spam'
    print(z)
    print(x)  #x points to same object with now .val set to 'spam'
