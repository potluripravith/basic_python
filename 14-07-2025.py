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

