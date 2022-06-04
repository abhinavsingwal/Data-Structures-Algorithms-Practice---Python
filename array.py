# Python Array Program
from array import *
# arrayName = array(typecode, [Initializers])
# Typecode are the codes that are used to define the type of value the array
# will hold. Some common typecodes used are as follow-
# Typecode         -            Value
# b - Represents signed integer of size 1 byte
# B - Represents unsigned integer of size 1 byte
# c - Represents character of size 1 byte
# i - Represents signed integer of size 2 bytes
# I - Represents unsigned integer of size 2 bytes
# f - Represents floating point of size 4 bytes
# d - Represents floating point of size 8 bytes

# Programs

# Create and print an array using Python.

from array import *
array1 = array('i',[10,20,30,40,50])

for x in array1:
    print(x)

# Accessing Array Element
# We can access each element of an array using the index of the element. The
# below code shows how to access an array element.

from array import *
array1 = array('i', [10,20,30,40,50])
print(array1[0])
print(array1[2])

# Instertion Operation

# Insert operation is to insert one or more data elements into an array. Based on the requirement, a new
# element can be added at the begining, end, or any given index of array.

# Here, we add a data element at the middle of the array using python in-built insert() method.

from array import *
array1 = array('i',[10,20,30,40,50])
array1.insert(1,60)

for x in array1:
    print(x)


# Delete Operation

# Deletion refers to removing an existing element from the array and re-organizing all
# elements of an array.

# Here, we remove a data element at the middle of the array using the python in-built remove() method.

from array import *
array1 = array('i',[10,20,30,40,50])
array1.remove(40)

for x in array1:
    print(x)


# Search Operation
# You can perform a search for an array element based on its value or its index.

# Here, we search a data element using the python in-built index() method.
from array import *

array1=array('i',[10,20,30,40,50])
print(array1.index(40))

# Update Operation

# Update operation refers to updating an existing element from the array at a given index.

# Here, we simply reassign a new value to the desired index we want to update.
from array import *
array1 = array('i',[10,20,30,40,50])
array1[2]=809
for x in array1:
    print(x)
