# -*- coding: utf-8 -*-
"""
CAR SuperClass

Petrol SubClass
Diesal SubClass
Electric SubClass
Hybrid SubClass

"""

# Define a class for my car

class Car(object):
# Construct car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.__engineSize = 0
        self.__cartype = ''
        self.__carfuel = ''
        self.__move = 0

#get variables

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage
    
    def getEngineSize(self):
        return self.__engineSize
    
    def getCartype(self):
        return self.__cartype

    def getCarfuel(self):
        return self.__carfuel
   
    def getMove(self):
        return self.__move

#set variables

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage
   
    def setEngineSize(self,enginesize):
        self.__engineSize = enginesize
    
    def setCartype(self,cartype):
        return self.__cartype

    def setCarfuel(self,carfuel):
        return self.__carfuel

    def setMove(self,move):
        return self.__move


# action methods


# Subclass- petrol car

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

# Subclass- diesal car

class DiesalCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

# Subclass- electric car

class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

# Subclass- hybrid car

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__numberCylinders = 1
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
    
    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value



