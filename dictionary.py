# In Dictionary  each key is separated from its value by a color (:), the items
# are separated by commas, and the whole thing is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces,
# like this - {}.
# Keys are unique within a dictionary while values may not be. The values of a dictionary
# can be of any type, but the keys must be of an immutable data type such as strings, numbers
# or tuples
# Accessing Values is as follows --
dict = {'Name':'Zara','Age':7,'Class':'First'}
print("dict['Name']: ",dict['Name'])
print("dict['Age']: ",dict['Age'])
# If we attempt to access a data item with a key, which is not part of the dictioanry
# we get an error as follow -
dict = {'Name':'Zara','Age':7,'Class':'First'}
# print("dict['Alice']: ",dict["Alice"])

# Updating Dictionary
 # You can update a dictionary by adding a new entry or a key-value pair,
# modifying an existing entry, or deleting an existing entry as shown below in the
# simple example -
dict={'Name':'Zara','Age':7,'Class':'First'}
dict['Age']=8  # update existing entry
dict['School']='DPS School' # Add new entry
print("dict['Age']: ",dict['Age'])
print("dict['School']: ",dict['School'])

# Delete Dictionary Elements
# You can either remove individual dictionary elements or clear the entire
# contents of a dictionary. You can also delete entire dictionary in a single operation.
# To explicitly remove an entire dictionary, just use the del statement. A simple
# example is as mentioned below -
dict={'Name':'Zara','Age':7,'Class':'First'}
del dict['Name'] # remove entry with key 'Name'
dict.clear() # remove all entries in dict
del dict # delete entire dictionary

print("dict['Age']: ",dict['Age'])
print("dict['School']: ",dict['School'])
# Properties of Dictionary Keys
# Dictionary values have no restrictions, They can be any arbitary Python object, either
# standard objects or user-defined objects. However, same is not true for the keys.

dict={'Name':'Zara','Age':7,'Name':'Manni'}
print("dict['Name']: ",dict['Name'])
