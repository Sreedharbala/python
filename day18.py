#day18 feb14
#Encapsulation
#encapsulation allows for the hiding of the internal state and requiring all interactions
#to occur through very defined interfaces these concept helps in acheiving data abstraction, data hiding and modularity in software design
#promoting better code maintainance and reducing complexity.

class car:
    def __init__(self,make,model,year):
          self.__make = make
          self.__model = model
          self.__year = year
          self.__is_started = False

    def start_engine(self):
        self.__is_started=True
        print("engine started")

    def stop_engine(self):
        self.__is_started = False
        print("engine stopped")

    def repair_engine(self):
        self.__is_started= float
        print("engine repaired")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def is_engine_started(self):
        return self.__is_started

my_car = car("toyota","camy",2020)
print("MAKE:", my_car.get_make())
print("MODEL:", my_car.get_model())
print("YEAR:", my_car.get_year())
my_car.repair_engine()



my_car.start_engine()
print("engine started?", my_car.is_engine_started())

my_car.stop_engine()
print("engine stopped?", my_car.is_engine_started())

my_car.repair_engine()
print("engine repaired?", my_car.is_engine_started())