oops: https://www.geeksforgeeks.org/interview-prep/oops-interview-questions/
1. Encapsulation
Wrapping data and methods into a single class and restricting direct access to data.
Real-Life Example
ATM Machine Balance is hidden from users. Users can only deposit or withdraw using provided options.
Python Example

class BankAccount:
    def __init__(self):
        self.__balance = 1000   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(500)
print(acc.get_balance())  # 1500
Interview Answer

"Encapsulation means hiding data and controlling access through methods. For example, in an ATM, users cannot directly change the account balance; they can only use deposit or withdraw options."

2. Inheritance
Definition

A child class acquires properties and methods from a parent class.

Real-Life Example

Vehicle → Car

Car is a Vehicle.
Car gets common features like start(), stop() from Vehicle.
Python Example
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

c = Car()
c.start()  #vechicle started

Interview Answer
"Inheritance allows code reuse. For example, a Car inherits common properties from Vehicle instead of writing them again."

3. Polymorphism
Same method name behaves differently for different objects.
Real-Life Example
Animal Sounds
Dog → Bark
Cat → Meow
Same method: sound()

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.sound()   

#Bark
#Meow
"Polymorphism means one interface with multiple forms. For example, the sound() method produces different outputs for Dog and Cat."

4. Abstraction
Showing only essential details and hiding implementation.
Real-Life Example
Car Driving
Driver uses steering, brake, accelerator.
Driver doesn't need to know engine internals.
Python Example
  
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

c = Car()
c.start()
#Car Started
