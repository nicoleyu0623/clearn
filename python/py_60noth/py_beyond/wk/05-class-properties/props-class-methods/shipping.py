import iso6346

#base class
class ShippingContainer:

    #class constants
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337



    @staticmethod   #static methods are not bound to class logic
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @classmethod  #classmethods are logically bound to a class
    def _get_next_serial(cls):  #cls is a reserved word for class
        result = cls.next_serial
        cls.next_serial += 1  #modiifie class next_serial = 1337
        return result

    # *args and **kwargs will be forwared to inherited classess
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)


    def __init__(self, owner_code, length_ft, contents): #self is for instance
        self.contents = contents          #instance attributes
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial = ShippingContainer._get_next_serial())

    #class string representation
    def __repr__(self):
        return 'ShippingContainer(bic={}, length={}, contents={}'\
                .format(self.bic, self.length_ft, self.contents)

    #property as decorator
    @property
    def volume_ft3(self):  #HEIGHT_FT is accessed with FQDN
        return ShippingContainer.HEIGHT_FT * \
               ShippingContainer.WIDTH_FT * self.length_ft

##derived class
class RefrigeratedShippingContainer(ShippingContainer):

    #additional class agtribute
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100.99

    ##static method overwritten in derived class
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R') #additional param

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9



    def __init__(self, owner_code, length_ft, contents, celsius ):
        #NB! calling __init__ from parent
        super().__init__(owner_code, length_ft, contents)
        self._celsius = celsius #additional param
                                #_celsius naming  = it's not part of public API

    def __repr__(self):
        return 'RefrigeratedShippingContainer(bic={}, length={}, contents={}, celcius={}'\
                .format(self.bic, self.length_ft, self.contents, self.celsius)



    ##additonal property as decorator, getter
    @property
    def celsius(self):
        return self._celsius


   #setter decorator
    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    #this property calls a static function
    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)


    #this property access the parent property
    @property
    def volume_ft3(self):
        return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3



#doubly derived class
class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    def __repr__(self):
        return 'HeatedRefrigeratedShippingContainer(bic={}, length={}, contents={}, celcius={}'\
                .format(self.bic, self.length_ft, self.contents, self.celsius)

    #FQDN from parent class
    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        RefrigeratedShippingContainer.celsius.fset(self, value)

