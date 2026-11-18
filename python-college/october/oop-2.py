class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def travel_time(self, distance = 300):
        return distance / self.speed


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_per_100km):
        super().__init__(brand, speed)
        self.fuel_per_100km = fuel_per_100km

    def fuel_needed(self, distance):
        return distance / 100 * self.fuel_per_100km


class Bicycle(Vehicle):
    def __init__(self, brand, fitness_level):
        speed = 10 + fitness_level * 2
        super().__init__(brand, speed)
        self.fitness_level = fitness_level


class Plane(Vehicle):
    def __init__(self, brand, speed, takeoff_landing_time=1.5):
        super().__init__(brand, speed)
        self.takeoff_landing_time = takeoff_landing_time

    def travel_time(self, distance):
        return super().travel_time() + self.takeoff_landing_time


car = Car("Volkswagen", 80, 7)
bike = Bicycle("Velik", 3)
plane = Plane("Aircar", 700)

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