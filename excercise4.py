class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity ):
        self.seating_capacity = capacity
        return f"Seating capacity of this vehicle is {capacity}"

class Bus(Vehicle):
    pass
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50)

mercedes = Bus(220, 60)
print(mercedes.seating_capacity())