QUESTION 1-  What are the five key concepts of Object-Oriented Programming (OOP)?

SOLUTION 1-
These five key concepts—encapsulation, abstraction, inheritance, polymorphism, and composition—form the foundation 
of Object-Oriented Programming and help create modular, reusable, and maintainable code. Each concept plays a crucial 
role in designing software systems that are efficient and easy to manage.

EXAMPLE:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

EXAMPLE:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)








QUESTION 2- Write a Python class for a `Car` with attributes for `make`, `model`, and `year`. Include a method to display
the car's information.

SOLUTION 2-

class Car:
    def __init__(self, make, model, year):
        """Initialize the car with its make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Display the car's information."""
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Example usage
if __name__ == "__main__":
    # Creating an instance of the Car class
    my_car = Car("Toyota", "Camry", 2022)

    # Displaying the car's information
    my_car.display_info()

OUTPUT:
Car Information: 2022 Toyota Camry







QUESTION 3- Explain the difference between instance methods and class methods. Provide an example of each.

SOLUTION 3-
Instance Methods
Definition: Instance methods are the most common type of methods. They operate on instances of the class and can access and modify instance attributes.
First Parameter: The first parameter of an instance method is always self, which refers to the instance calling the method.
Access: Instance methods can access instance variables and class variables.

EXAMPLE:
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def bark(self):
        """Instance method that makes the dog bark."""
        return f"{self.name} says Woof!"

# Creating an instance of Dog
my_dog = Dog("Buddy", 3)

# Calling the instance method
print(my_dog.bark())  # Output: Buddy says Woof!


Class Methods
Definition: Class methods are methods that belong to the class itself rather than any particular instance. They can be used for factory methods, which instantiate objects in a specific way.
First Parameter: The first parameter of a class method is always cls, which refers to the class itself, not an instance of the class.
Decorator: Class methods are defined using the @classmethod decorator.
Access: Class methods can access class variables but cannot access instance variables directly unless they have an instance reference.

EXAMPLE:
class Dog:
    species = "Canis lupus familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        """Class method that returns the species of the dog."""
        return cls.species

# Calling the class method without creating an instance
print(Dog.get_species())  # Output: Canis lupus familiaris






QUESTION 4-How does Python implement method overloading? Give an example.

SOLUTION 4-
Python does not support traditional method overloading as seen in some other languages, but you can achieve similar functionality through:
Default arguments: Allowing methods to accept a varying number of arguments.
Variable-length arguments: Using *args to accept any number of positional arguments.
Type checking: Implementing conditional logic to handle different types of arguments within a single method.

EXAMPLE:
class Calculator:
    def add(self, a, b=0, c=0):
        """Add two or three numbers."""
        return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Calling the method with different numbers of arguments
print(calc.add(5, 10))      # Output: 15 (adds two numbers)
print(calc.add(5, 10, 15))  # Output: 30 (adds three numbers)






QUESTION 5-What are the three types of access modifiers in Python? How are they denoted?

SOLUTION 5-
1. Public Access Modifier
Definition: Members declared as public are accessible from both inside and outside the class. By default, all class members are public unless specified otherwise.
Denotation: Public members are declared without any prefix.

2. Protected Access Modifier
Definition: Members declared as protected are intended to be accessible only within the class and by subclasses (derived classes). However, they can still be accessed from outside the class by using an instance, though this is discouraged.
Denotation: Protected members are denoted by a single underscore prefix (_).

3. Private Access Modifier
Definition: Members declared as private are accessible only within the class in which they are defined. They cannot be accessed or modified directly from outside the class.
Denotation: Private members are denoted by a double underscore prefix (__).






QUESTION 6- Describe the five types of inheritance in Python. Provide a simple example of multiple inheritance.

SOLUTION 6-
These five types of inheritance in Python allow for flexible and organized code design:

Single Inheritance: A single subclass inherits from one superclass.
Multiple Inheritance: A subclass inherits from multiple superclasses.
Multilevel Inheritance: A subclass inherits from a superclass, which itself is a subclass of another superclass.
Hierarchical Inheritance: Multiple subclasses inherit from a single superclass.
Hybrid Inheritance: A combination of two or more types of inheritance.

EXAMPLE MULTIPLE Inheritance:

class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming deep!"

class Duck(Flyer, Swimmer):  # Duck inherits from both Flyer and Swimmer
    def quack(self):
        return "Quack!"

# Usage
my_duck = Duck()
print(my_duck.fly())  # Output: Flying high!
print(my_duck.swim())  # Output: Swimming deep!
print(my_duck.quack())  # Output: Quack!



QUESTION 7-What is the Method Resolution Order (MRO) in Python? How can you retrieve it programmatically?

SOLUTION 7-
MRO defines the order in which Python searches for methods and attributes in a class hierarchy.
The C3 linearization algorithm is used to calculate the MRO.
You can retrieve the MRO of a class using the mro() method or the __mro__ attribute.

Retrieving Method Resolution Order Programmatically
Using the mro() method:
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


Using the __mro__ attribute:
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)






QUESTION 8-Create an abstract base class `Shape` with an abstract method `area()`. Then create two subclasses
`Circle` and `Rectangle` that implement the `area()` method.

SOLUTION 8-
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print(f"Area of Circle: {circle.area():.2f}")      # Output: Area of Circle: 78.54
    print(f"Area of Rectangle: {rectangle.area():.2f}") # Output: Area of Rectangle: 24.00

Explanation:
Abstract Base Class (Shape):

Inherits from ABC, the base class for defining Abstract Base Classes.
Contains the abstract method area() which subclasses must implement.

Subclass (Circle):

Takes the radius as an argument during initialization.
Implements the area() method to calculate the area of a circle using the formula πr*

Subclass (Rectangle):

Takes width and height as arguments during initialization.
Implements the area() method to calculate the area of a rectangle using the formula width×height


Example Usage:

Instances of Circle and Rectangle are created, and their area() methods are called to display the calculated areas.






QUESTION 9-Demonstrate polymorphism by creating a function that can work with different shape objects to calculate
and print their areas.

SOLUTION 9-
Polymorphism is the ability in programming to use a single function to process different types of objects in a unified way. 
In the context of object-oriented programming, it means that objects of different classes can be treated through the same 
interface. Here, we will use polymorphism by creating a function that can accept different Shape objects 
(like Circle, Rectangle, etc.) and calculate their area by calling their respective area() method.


from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function that demonstrates polymorphism
def print_area(shape):
    # The same function works for all shapes
    print(f"The area is: {shape.area():.2f}")

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(4, 5)
    
    # Polymorphic behavior: same function handles different types of shapes
    print_area(circle)     # Output: The area is: 78.54
    print_area(rectangle)  # Output: The area is: 24.00
    print_area(triangle)   # Output: The area is: 10.00

OUTPUT:
The area is: 78.54
The area is: 24.00
The area is: 10.00



QUESTION-10-  Implement encapsulation in a `BankAccount` class with private attributes for `balance` and
`account_number`. Include methods for deposit, withdrawal, and balance inquiry.

SOLUTION 10-
Encapsulation in object-oriented programming is the concept of restricting direct access to some of an object's 
components, usually by making class attributes private. Private attributes in Python are denoted by prefixing the 
attribute name with double underscores (__). We can access or modify these private attributes only through public methods 
(getters, setters, or other methods).

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    # Method to check balance
    def get_balance(self):
        return self.__balance

    # Method to get account number (if needed)
    def get_account_number(self):
        return self.__account_number

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456789", 1000)  # Create an account with an initial balance of 1000
    
    # Check initial balance
    print(f"Initial balance: {account.get_balance()}")  # Output: Initial balance: 1000
    
    # Deposit money
    account.deposit(500)  # Output: Deposited: 500
    print(f"Balance after deposit: {account.get_balance()}")  # Output: Balance after deposit: 1500
    
    # Withdraw money
    account.withdraw(300)  # Output: Withdrew: 300
    print(f"Balance after withdrawal: {account.get_balance()}")  # Output: Balance after withdrawal: 1200
    
    # Attempt an invalid withdrawal
    account.withdraw(2000)  # Output: Insufficient balance or invalid amount.
    
    # Check account number (optional)
    print(f"Account Number: {account.get_account_number()}")








QUESTION-11- Write a class that overrides the `__str__` and `__add__` magic methods. What will these methods allow
you to do?

SOLUTION 11-
In Python, magic methods (also known as dunder methods because they are surrounded by double underscores) are special 
methods that define the behavior of objects for built-in operations. Two commonly overridden magic methods 
are __str__ (for string representation of objects) and __add__ (for addition of objects).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Override __str__ to provide a readable string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Override __add__ to define addition of two Vector objects
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

# Example usage
if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    
    # Printing the vectors
    print(v1)  # Output: Vector(2, 3)
    print(v2)  # Output: Vector(4, 5)
    
    # Adding two vectors
    v3 = v1 + v2
    print(v3)  # Output: Vector(6, 8)

Output for print(v1):


Vector(2, 3)

Output for v1 + v2:


Vector(6, 8)








QUESTION 12- Create a decorator that measures and prints the execution time of a function.

SOLUTION 12-
In Python, a decorator is a function that wraps another function to extend or alter its behavior without modifying its code. 
To create a decorator that measures and prints the execution time of a function, we can use the time module to track the start 
and end times of the function's execution.

import time

# Decorator to measure execution time
def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Get the current time before function execution
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Get the time after function execution
        execution_time = end_time - start_time  # Calculate the time taken
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result  # Return the original function's result
    return wrapper

# Example usage of the decorator
@execution_time_decorator
def slow_function():
    time.sleep(2)  # Simulating a function that takes time (e.g., 2 seconds)
    print("Finished slow function")

@execution_time_decorator
def add_numbers(a, b):
    return a + b

# Example usage
if __name__ == "__main__":
    slow_function()  # This will print the execution time
    result = add_numbers(5, 7)  # Execution time for the addition
    print(f"Result of add_numbers: {result}")

OUTPUT:
Finished slow function
Execution time of slow_function: 2.002345 seconds
Execution time of add_numbers: 0.000001 seconds
Result of add_numbers: 12





QUESTION 13- Explain the concept of the Diamond Problem in multiple inheritance. How does Python resolve it?

SOLUTION 13-
The Diamond Problem arises in object-oriented programming languages that allow multiple inheritance, where a 
class can inherit from more than one base class. This problem occurs when a class inherits from two (or more) 
classes that share a common ancestor, creating an ambiguity in the inheritance chain.


Diamond Problem Illustration:
Consider the following class hierarchy:
      A
     / \
    B   C
     \ /
      D

In this example:

Class B and Class C both inherit from Class A.
Class D inherits from both Class B and Class C.
Now, if Class A defines a method (say method()), and Class D tries to call that method, there's ambiguity:

Should Class D inherit method() from Class B or from Class C?
What if both B and C override method() differently?
This ambiguity is referred to as the Diamond Problem.

# Diamond problem example
class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    pass

# Create an instance of class D
d = D()
d.method()

# Show the Method Resolution Order
print(D.__mro__)







QUESTION 14-Write a class method that keeps track of the number of instances created from a class.

SOLUTION 14-

To keep track of the number of instances created from a class, We can define a class method that increments 
a class-level attribute every time a new instance is created. Class methods are defined using the @classmethod 
decorator and have access to the class itself (passed as cls).

class InstanceCounter:
    instance_count = 0  # Class attribute to track the number of instances

    def __init__(self):
        # Increment the class-level counter every time a new instance is created
        InstanceCounter.instance_count += 1

    @classmethod
    def get_instance_count(cls):
        # Class method to return the current instance count
        return cls.instance_count

# Example usage
if __name__ == "__main__":
    # Creating instances of the class
    obj1 = InstanceCounter()
    obj2 = InstanceCounter()
    obj3 = InstanceCounter()

    # Get the current instance count using the class method
    print("Number of instances created:", InstanceCounter.get_instance_count())


OUTPUT:
Number of instances created: 3







QUESTION 15-. Implement a static method in a class that checks if a given year is a leap year.

SOLUTION 15- 
In Python, a static method is a method that does not depend on the class or instance attributes. Static methods are defined using 
the @staticmethod decorator. They do not take self or cls as their first argument, and they behave like regular functions that 
happen to live inside a class.
    
class DateUtils:
    @staticmethod
    def is_leap_year(year):
        # Check if the year is divisible by 4 and (divisible by 400 or not divisible by 100)
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            return True
        return False

# Example usage
if __name__ == "__main__":
    year = 2024
    if DateUtils.is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


OUTPUT:
2024 is a leap year.

In this example, the is_leap_year() method checks if the year 2024 is a leap year and prints the result accordingly. 
You can call this method on any year you want to check, and it will return True if it’s a leap year or False otherwise.





