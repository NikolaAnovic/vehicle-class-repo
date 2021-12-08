class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

mercedes = Bus(220, 60)
print("Bus speed:", mercedes.max_speed, "Bus mileage:", mercedes.mileage)