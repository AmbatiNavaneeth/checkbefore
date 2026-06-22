oops: https://www.geeksforgeeks.org/interview-prep/oops-interview-questions/

Quick Comparison Matrix
Scenario                                           Where is it?          How to call it?  Do you wrap the call in print()?
Standalone Function (with return)             Outside a classgreet()       Yes, to see the output: print(greet())
Standalone Function (with print)              Outside a classgreet()        No, just call it directly: greet()
Class Method (with return)                 Inside a classobject.greet()    Yes, to see the output: print(object.greet())
Class Method (with print)                  Inside a classobject.greet()   No, just call it directly: object.greet()

1. Outside a Class (Standalone Functions)When a function is not inside a class, you call it by writing its name followed by parentheses ().
If the function uses return:The function calculates a value and hands it back to you silently. To see it on your screen, you must wrap the entire call inside a print() statement.python
def get_hello():
    return "Hello from outside!"  # Hands over data silently 
# You must print the result to see it
print(get_hello())  # Output: Hello from outside!

If the function already uses print() inside:
The function itself is responsible for showing the message. You should not wrap it in another print(), otherwise Python will display your message and then print None (because the function didn't return anything).python
def show_hello():
    print("Hello from outside!")  # It displays the text itself


# Call it directly without wrapping it in print()
show_hello()  # Output: Hello from outside!
Use code with caution.
                                                                                                                                                                       
2. Inside a Class (Methods)When a function is inside a class, it is called a method. To use it, you must first create an object from that class (called instantiating) and use dot notation (object.method()). 
You also include self in the function definition so it can interact with the object.
-->If the method uses return:
Just like standalone functions, it hands back data silently. You wrap the object-dot-method call inside a print().
                                                            
class Greeter:
    def get_welcome(self):  # 'self' is required inside a class
        return "Welcome from inside a class!
# 1. Create the object
my_greeter = Greeter()
# 2. Call and print the returned value
print(my_greeter.get_welcome())  # Output: Welcome from inside a class!

-->If the method already uses print() inside:
You call the object-dot-method directly on its own line without wrapping it in a print() statement.pythonclass Greeter:
    def show_welcome(self):
        print("Welcome from inside a class!")  # Displays text directly
# 1. Create the object
my_greeter = Greeter()
# 2. Just call it directly
my_greeter.show_welcome()  # Output: Welcome from inside a class!



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
