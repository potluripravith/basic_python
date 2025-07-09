### Decorators are function transformers that modify  the behavior of functiona/classes without changing their source code
## It will also work for open/closed pricinple

def decorator(func):
    def wrapper():
        func()
        print("How can i Help you?")
    
    return wrapper

@decorator
def greet():
    print ("Hello!")
    
    
greet()

### Time Decorator
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time Taken : {end-start} seconds")
    return wrapper

@timer
def function():
    time.sleep(1.5)
    
function()

#### Metaclasses are called as classes of classes - they define how classes themselves behave.
####Metaclasses create classes just like classes create objects
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    def say_hello(self):
        print("Hello")

### Asyncio for concurrent programming using async/wait syntax
## create a task async def corountine function await pauses the cureent func .run() main entry point
import asyncio
async def task(name,delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds")
    
async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )

asyncio.run(main())

### Context Managers that set something lets as use it and cleans it automatically
# with open("data.txt", "r") as file:
#     content = file.read()
    ## no need of file.close() it is closed automatically
    
#### Protcols support duck typing with static type safety

from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

class File:
    def close(self) -> None:
        print("File closed")

class Socket:
    def close(self) -> None:
        print("Socket closed")

def shutdown(resource: SupportsClose) -> None:
    resource.close()

# Both work despite different types!
shutdown(File())   
shutdown(Socket()) 