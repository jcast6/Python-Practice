from array import *

arr1 = array('i', [10, 20, 30, 40])

for x in arr1:
    print(x)

print('\naccessing array element: ')
print(arr1[0])
print(arr1[2])

print('\ninsertion operation: ')
arr1.insert(1, 60)

for x in arr1: 
    print(x)

print('\ndeletion operation: ')
arr1.remove(40)

for x in arr1:
    print(x)

print('\nsearch operation: ')
searched_element = 20
print ('searched element: ',searched_element, ' index:', arr1.index(20))
