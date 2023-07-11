#Problem 14 (11-07-2023)
#Problem Statement: Write a python program to create a class Vehicle and display the properties of the vehicle like max speed,mileage and seating capacity. 
#Additionally, create two objects of the Vehicle class object that should have a max speed of 200kph and mileage of 50000kmpl with five seating capacities
class Vehicle:
    color = 'white'
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seat(self,seat_capacity):
        self.seat_capacity = seat_capacity
            
    def display_properties(self):
        print(f"Properties of the vehicle.")
        print(f"Color:{self.color}\nMaximum speed: {self.max_speed}")
        print(f"Mileage: {self.mileage}\nSeating Capacity: {self.seat_capacity}")

car1 = Vehicle(max_speed = 200,mileage = 50000)
car1.seat(5)
car1.display_properties()
