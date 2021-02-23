# import the json library
import json;

# python object which is an array
myList = ["Solomon", "Ndifereke", "Aniefiok"];

# python object which is a dictionary
myDictionary = {"name":"Solomon", "FirstName":"Ndifereke"};

# convert python object which is a list to a string
myList_to_String = json.dumps(myList);
# print the type
print(myList_to_String);

# convert python object which is a dictionary to a string
myDictionary_to_String = json.dumps(myDictionary);
# print the type=>result is a string
print(myDictionary_to_String);

# convert string back to python object using the loads function
myList_to_List = json.loads(myList_to_String);
# print the type => result is a list
print(type(myList_to_List));

# convert string back to python object using loads function
myDictionary_to_Dictionary = json.loads(myDictionary_to_String);
# print the type
print(myDictionary_to_Dictionary)

