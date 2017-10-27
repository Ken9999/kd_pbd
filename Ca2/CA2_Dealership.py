# -*- coding: utf-8 -*-
"""
Dealership Class
"""
from CA2_Car import ElectricCar, PetrolCar, HybridCar, DiesalCar

#Dealership Class
# keeps an inventory of Petrol, Diesal, Electric and Hybrid Cars
# rented and returned by Customers 
class Dealership(object):
    # Construct Inventory Lists
    def __init__(self):
        self.petrol_carlist = []
        self.diesal_carlist = [] 
        self.electric_carlist = []
        self.hybrid_carlist = []
    # Current stock is input from Carpool CSV file  
    # csv file contains -
    # 20 Petrol Cars 8 Diesal Cars  
    # 4 Electric Cars and 8 Hybrid Cars --- Total 40 Cars
    def create_current_stock(self):
        # Populate inventory list for each car type    
        fhand = open('C:/Users/Ken/Downloads/carpool.csv','r')
        for line in fhand:
            line = line.rstrip().split(',')
            if line[4] == 'P':
                self.petrol_carlist.append(PetrolCar)
            elif line[4] == 'D':
                self.diesal_carlist.append(DiesalCar)
            elif line[4] == 'E':
                self.electric_carlist.append(ElectricCar)
            elif line[4] == 'H':
                self.hybrid_carlist.append(HybridCar)
        #close file
        fhand.close()   
    #Check Stock Amounts
    def stock_count(self):
        petrol_cars_in_stock = str(len(self.petrol_carlist)) 
        diesal_cars_in_stock = str(len(self.diesal_carlist)) 
        electric_cars_in_stock = str(len(self.electric_carlist)) 
        hybrid_cars_in_stock = str(len(self.hybrid_carlist)) 
        print('petrol cars in stock ' + petrol_cars_in_stock)
        print('diesal cars in stock ' + diesal_cars_in_stock)
        print('electric cars in stock ' + electric_cars_in_stock)
        print('hybrid cars in stock ' + hybrid_cars_in_stock)
        # Total amount of cars is 40 - if all rented out - print message
        if int(petrol_cars_in_stock) + int(diesal_cars_in_stock) +\
           int(electric_cars_in_stock) + int(hybrid_cars_in_stock) == 0:
           print('Sorry nothing to rent, please try again later ')
    #Rent Car
    def rent(self, car_list, amount):
        # If the amount of cars requested is more 
        # than number of cars in stock - return message  
        if len(car_list) < amount:
            print ('Not enough cars in stock')
            return
        total = 0
        #remove cars from list when cars are rented
        while total < amount:
           car_list.pop()
           total = total + 1 
    #Return Car
    def return_car(self, car_list, amount):
        total = 1
        #add cars to list when cars are returned
        while total <= amount:
           car_list.append(total)
           total = total + 1            
    #Rental Car Process
    def rental_car_process(self):
        # Present Options to User 
        # Option A - Rent a Car
        # Option B - Return a Car
        answer = input('********** Aungier Car Rentals *************'+'\n'\
                       'Please input A for Rent or B for Return ==> ')
        # Rent a Car - Option A
        if answer == 'A':
          answer = input('What type of car would you like -' +'\n' + \
                         'Please enter p for a Petrol Car'+\
                         ' or d for a Diesal Car'+\
                         ' or e for an Electric Car'+\
                         ' or h for a Hybrid Car')
          if answer == 'p' or answer=='d' or answer=='e' or answer =='h':
            amount = int(input('How many cars would you like to rent ?'))
            if answer == 'p':
                self.rent(self.petrol_carlist, amount)
            elif answer == 'd':
                self.rent(self.diesal_carlist, amount)
            elif answer == 'e':
                self.rent(self.electric_carlist, amount)
            elif answer == 'h':
                self.rent(self.hybrid_carlist, amount)
          # Invalid Option selected
          else:
                print('Not a valid option -valid options are p/d/e/h')
        # Return Rental Car - Option B
        elif answer == 'B':
          answer = input('What type of car are you returning -'+'\n'+ \
                         'Please enter p for a Petrol Car'+\
                         ' or d for a Diesal Car'+\
                         ' or e for an Electric Car'+\
                         ' or h for a Hybrid Car')    
          if answer == 'p' or answer=='d' or answer=='e' or answer =='h':
            amount = int(input('How many cars would you like to return ?'))
            if answer == 'p':
                self.return_car(self.petrol_carlist, amount)
            elif answer == 'd':
                self.return_car(self.diesal_carlist, amount)
            elif answer == 'e':
                self.return_car(self.electric_carlist, amount)
            elif answer == 'h':
                self.return_car(self.hybrid_carlist, amount) 
          # Invalid option selected
          else:
                print('Not a valid option -valid options are p/d/e/h')
        self.stock_count()
#Main 
if __name__ == '__main__':
    #Create Aungier Dealership
    aungier_dealership = Dealership()
    aungier_dealership.create_current_stock() 
    #Process as User Requests
    proceed = 'y'
    while proceed == 'y':
        aungier_dealership.rental_car_process()
        proceed = input('Continue - Please Enter - y/n ') 

