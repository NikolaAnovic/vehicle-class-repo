class Vehicle:
    
    def __init__(self, max_speed, mileage,capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare_method(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass
    def fare_method(self):
        amount = super().fare_method()
        amount += amount * 10/100
        return int(amount)

mercedes = Bus(220, 60, 50)
print("Bus fare is",mercedes.fare_method())