class Car:
    #Class attributes 
    all_cars = {}
    total_cars = 0
    _next_id = 1

    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services =[]
        self._id = Car._next_id
        Car._next_id += 1
        Car.total_cars += 1
        Car.all_cars[self._id] = self

        #ID
    @property
    def id(self):
        return self._id

    #make
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    #model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    #year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    #mileage
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        self._mileage =value

    @property
    def services(self):
        return list(self._services)

    @services.setter
    def services(self, value):
        self._services = list(value)

