# SOlid Principles
# 1)Single Resiponsibility Principle 2) Open and Closed Principle 3) Liskov substitution principle 4) interface segregation  principle 5) dependency inversion principle 
# 1) single Resiponsibility Principle defines that class must have that same reponsibility
## It is impoertant a appears in a class we will know where to look  no need of whole code
### so slpit the functions 
### sometimes there may have dependency trap in the class 
#When i split the code in srp for responsibilities
# Then we can use abstraction class or dividing it into multiple classes or dependency injection


# Open/Closed Principle : when we done writing function it should be open for extension but not for chaning existing code:
## Instead of commiting anything give only the general function in abstraction and then do in own functions


## Liskov Substitution Principle subtypes has to be substitutiton for their base types without changing the corectness of the program
### if we are inheratient the a class which super class we should the data type of super class in sub class we should not change it and also the excepetion behaviour of the function


# Interface segregation principle clients should not forced to depend on interfaces they don't use here we cana use protcols

### dependency inversion prinicple
#### high level modules should not depend on low level modules both should depend on abstractions


# Classes  is a blueprint and objects are instances and
## inheritance we can inheritate class from one another multiple inheritance 
#### Encapsulationprivate if dont want it in inheritance class also or we can use protected which is similar to privaate can be used in subclasses also 
#### Polymorphism where it is of three types duck typing where it behaves what is given and another is method overriding where we can overrinde function in super class in subclass and operator overloading where can change the existing overloading
#### abstraction which is done desgin level implementation 
# 1. List Comprehensions
# List comprehensions are a concise way to create lists using a single line of code, typically written as [expression for item in iterable if condition]. They are important because they make your code shorter, cleaner, and more readable when transforming or filtering elements in a list. List comprehensions are especially useful when you want to build new lists based on existing sequences, such as squaring all even numbers in a range or extracting specific data from a list of dictionaries.

# 2. Decorators
# Decorators are functions that wrap around other functions to modify or extend their behavior without changing their original code. They are important for writing reusable and modular enhancements, such as logging, timing, access control, or memoization. Decorators are widely used in frameworks like Flask and Django to manage routing, permissions, and middleware behavior.


# 3. Protocols (from typing)
# Protocols are a way to define structural subtyping in Python, meaning a class can be considered compatible with a protocol if it implements the required methods or properties, regardless of inheritance. They’re important in statically typed Python code for flexibility and clarity, enabling better type checking and interface enforcement. Protocols are often used when writing generic functions that can accept any object that behaves in a certain way (duck typing with type hints).

# 4. Closures
# Closures are inner functions that capture and remember the state of variables from their enclosing scope even after the outer function has finished executing. They are important for encapsulating behavior with state, especially in callback functions or decorators. Closures are typically used when you need a function with some memory of its environment, such as in counter functions or lazy evaluation patterns.

# 5. Context Managers
# Context managers handle setup and cleanup actions automatically, typically used with the with statement (e.g., with open("file.txt") as f:). They are important for managing resources like files, network connections, or database sessions safely and efficiently. Context managers ensure that resources are properly closed or released, even if an exception occurs, making your code more robust and clean.

# 6. Metaclasses
# Metaclasses are classes of classes that control the creation and behavior of other classes. They are an advanced topic useful when you want to customize class creation, such as enforcing design patterns, automatically registering classes, or injecting attributes. Though rarely used in day-to-day coding, metaclasses are powerful tools for building frameworks, libraries, or internal tools that need to manipulate class structures at a higher level.

# 7. Asynchronous Programming (asyncio)
# Asynchronous programming allows functions to run concurrently without blocking the execution of other tasks, often using async and await keywords. It’s important for building high-performance applications that deal with I/O-bound operations like APIs, file access, or web servers. Asynchronous programming is commonly used in modern web frameworks and systems that handle thousands of requests efficiently.

# 8. Lambda Functions
# Lambda functions are anonymous, one-line functions defined using the lambda keyword. They are useful for writing short, throwaway functions without formally defining a def block. Lambdas are important in functional programming or whenever a small function is needed temporarily, such as with map(), filter(), or in sorting with custom keys.
