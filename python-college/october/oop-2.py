class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def travel_time(self, distance):
        return distance / self.speed


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_per_100km):
        self.brand = brand
        self.speed = speed
        self.fuel_per_100km = fuel_per_100km

    def fuel_needed(self, distance):
        return distance / 100 * self.fuel_per_100km


class Bicycle(Vehicle):
    def __init__(self, brand, fitness_level):
        self.brand = brand
        self.fitness_level = fitness_level
        self.speed = 10 + fitness_level * 2


class Plane(Vehicle):
    def __init__(self, brand, speed, takeoff_landing_time):
        self.brand = brand
        self.speed = speed
        self.takeoff_landing_time = takeoff_landing_time

    def travel_time(self, distance):
        return distance / self.speed + self.takeoff_landing_time


car = Car("Toyota", 90, 8)
bike = Bicycle("Giant", 3)
plane = Plane("Boeing", 800, 1.5)

vehicles = [car, bike, plane]
distance = 300

for v in vehicles:
    print(v.brand, "-", round(v.travel_time(distance), 2), "hours")

fastest = vehicles[0]
for v in vehicles:
    if v.travel_time(distance) < fastest.travel_time(distance):
        fastest = v

print("Fastest:", fastest.brand)
print("Fuel needed for the car:", car.fuel_needed(distance), "liters")