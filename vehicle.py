class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

KJA = Vehicle(531, 15)
print("Max Speed of Koenigsegg JA: ", KJA.max_speed, "km/h and mileage: ", KJA.mileage)