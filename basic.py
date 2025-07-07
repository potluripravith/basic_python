age = 38
name = "Alice"
height = 5.8
is_student = False
courses = ["Math", "Science"]

# Control Flow
if age >= 18:
    print("Adult")
elif age > 13:
    print("Teen")
    
else:
    print("Child")

# Loops
for course in courses:
    print(f"Studying {course}")

# Functions
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 4)) 

### Python Fundamentals 


try:
    result = 10/0
except ZeroDivisionError:
    print("cannot")
finally:
    print("cleanup complete")
    








































































