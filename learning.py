class Dog:
    species = "Cannis familiaris"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return f"{self.name} barks: {sound}"
        
class JackRussellTerrier(Dog):
    def speak(self,sound="Arf"):
        return super().speak(sound)
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass

buddy = Dachshund("Buddy",9)
miles = JackRussellTerrier("Miles",4)
jack = Bulldog("Jack",3)
jim = Bulldog("Jim",5)

print(buddy.name,buddy.age)
print(miles.speak())    
print(jim.speak("woof"))