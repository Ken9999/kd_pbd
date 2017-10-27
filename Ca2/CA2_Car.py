import unittest 
#Import CLasses for Testing 
from CA2_Car import Car, PetrolCar, ElectricCar,DiesalCar, HybridCar

# Test Car, PetrolCar, ElectricCar,DiesalCar, HybridCar - functionality
class TestCar(unittest.TestCase):
    #Test Car Class
    #test car mileage
    def test_car_mileage(self):
        self.car = Car() 
        self.assertEqual(0, self.car.getMileage())
        self.car.setMileage(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())
    #test car make 
    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
    #test car colour
    def test_car_colour(self):
        self.car = Car() 
        self.assertEqual('', self.car.getColour())
        self.car.setColour('yellow') 
        self.assertEqual('yellow', self.car.getColour())
    #test car engine size
    def test_car_engine_size(self):
        self.car = Car()
        self.assertEqual(0, self.car.getEngineSize())
        self.car.setEngineSize(2)
        self.assertEqual(2, self.car.getEngineSize())
    #Test Electric Car Class   
    #test electric car fuel cells
    def test_electric_car_fuel_cells(self): 
        electric_car = ElectricCar()
        self.assertEqual(1, electric_car.getNumberFuelCells())
        electric_car.setNumberFuelCells(4)
        self.assertEqual(4, electric_car.getNumberFuelCells())
    #Test Hybrid Car Class   
    #test hybrid car fuel cells
    def test_hybrid_car_fuel_cells(self): 
        hybrid_car = HybridCar()
        self.assertEqual(1, hybrid_car.getNumberFuelCells())
        hybrid_car.setNumberFuelCells(2)
        self.assertEqual(2, hybrid_car.getNumberFuelCells())
        hybrid_car.setNumberCylinders(2)
        self.assertEqual(2,hybrid_car.getNumberCylinders())
    #Test Petrol Car Class   
    #test petrol car cylinder size
    def test_petrol_car(self):
        petrol_car = PetrolCar()
        self.assertEqual(1, petrol_car.getNumberCylinders())
        petrol_car.setNumberCylinders(4)
        self.assertEqual(4, petrol_car.getNumberCylinders())
    #Test Diesal Car Class             
    #test diesal car cylinder size
    def test_diesal_car(self):
        diesal_car = DiesalCar()
        self.assertEqual(1, diesal_car.getNumberCylinders())
        diesal_car.setNumberCylinders(6)
        self.assertEqual(6, diesal_car.getNumberCylinders())

    # Main 
if __name__ == '__main__':
    unittest.main()
    
