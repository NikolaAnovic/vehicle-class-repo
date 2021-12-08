class Vehicle:
    color = "White"
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def seats_method(self,seating_capacity):
        self.seating_capacity = seating_capacity
        return f'This vehicle has a seating capacity of {seating_capacity}'
    def fare_method(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self,max_speed,mileage):
        super().__init__(max_speed,mileage)
    def seats_method(self,seating_capacity=50):
        return super().seats_method(seating_capacity=50)
    def fare_method(self):
        amount = super().fare_method()
        amount += amount * 10 /100
        return int(amount)

Mercedes = Bus(30,3000)
Audi = Vehicle(300,75000)
print(Mercedes.seats_method(),"and a fare of this vehicle is",Mercedes.fare_method())
print(Audi.seats_method("5"))