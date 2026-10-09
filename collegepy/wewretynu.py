class auto:
    def __init__(self, person):
        self.person = person

    def otkuda(self):
        if person == "white":
            return "evo mashina"
        elif person == "black":
            return "ukral?"

person = input("Whats your favorite color? ")

print(auto(person).otkuda())