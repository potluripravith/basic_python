### List Comprehensions
### instead of for loops we can do it in short for example

numbers = [1,3,5,7,9]

doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num*2)
    
print(doubled_numbers)

## if we have conditons to 

# new_list = [new_item for item in list if condition]
# new_item - the item with calculation on it 
# item - item(can be anything)
# list - the list
# condition 

numbers1 = [2,4,5] 
doubled_numbers = [num*2 for num in numbers1 if num > 3]
print(doubled_numbers)

## when there is complex implemnentation is requires then dont use or if it infinte then generators are useful dont use list comprehensions

####Lambda Funtions for one time use the take any number of aru=guments helps namespace clean and is useful the higher order functions

double = lambda x: x * 2 
add = lambda x,y : x+y
print(double([2,3]))
print(add(2,3))
max_value = lambda x,y : x if x > y else y 
print(max_value(6,5))



### list comprehensions create lists transformed colllections
### lambdas create fucntions 
students = [{"name": "Alice", "grade": 89}, {"name": "Bob", "grade": 72}]
def grade_filter(min_grade):
    return lambda student : student["grade"] > min_grade

filter_A = grade_filter(85)
filter_students = list(filter(filter_A,students))
print(filter_students)

numbers = [1,2,3,4]
doubled = map(lambda x: x*2,numbers)
print(list(doubled))
 
#### Context mangers is a construct that manages resources 
## most commonly used with open("file.txt") as f:
#data = read()
from contextlib import contextmanager
from typing import Any, Generator,IO

@contextmanager
def file_manager(path:str,mode:str)-> Generator[IO,Any,None]:
    file:IO =open(path,mode)
    print('Opening file ..')
    try:
        yield file
    except Exception as e:
        print(e)

    finally:
        print('Closing file')
        if file:
            file.close()

with file_manager('example.txt','r')as f:
    raise Exception('sunny did wrong')
   
    print(f.read())
## even exception is rasied code still close the file 
    
    
    

    


