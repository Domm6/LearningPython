# Learning the basics of python

# Practice print statements

import math
print("I am learnign how to print here:")
number = 0
print(number)
print("Hello World")
firstName = "Dominic"
secondName = "Parker"
print("Printing name with space:", firstName, secondName)
print("Printing with no spaces:", firstName, secondName, sep='')

# Data types
number = 100
other_number = 10.5
complex_num = 9+7j
bool_variable = False


# proves each of these data types
print(number, "is of type", type(number))
print(other_number, "is of type", type(other_number))
print(complex_num, "is of type", type(complex_num))
print(bool_variable, "is of type", type(bool_variable))

# Working with strings
sentence = "This is a sentence"
another_sentence = 'This is anohter sentence'
print('"', sentence, '"', "is a type of ", type(sentence))
print('"', another_sentence, '"', "is a type of", type(another_sentence))

# Slicing a string
exampleString = "This is a sentence"

print("example[2] = ", exampleString[2])
print("example[1:7]", exampleString[1:7])
print("example[:]", exampleString[:])
print("example[1:]", exampleString[3:])

# List
exampleList = [1, 2, 3, 4, 5,]
differentDataTypes = [1, 2, 3, "Hello World", False]

print(exampleList, "is a type of", type(exampleList))
print(differentDataTypes, "is a type of", type(differentDataTypes))

specificItem = exampleList[3]
listOfList = differentDataTypes[:2]
exampleList[0] = "python is easy"

print("\n")
print(specificItem)
print(listOfList)
print(exampleList)

# List Methods
thisList = [1, 2, 4, 6, 3, 6]
print("original list:", thisList)

thisList.append("added to the end of the list")
print("append method:", thisList, "\n")

thisList.insert(3, False)
print("inser method:", thisList)

thisList.remove(1)
print("remove method:", thisList)

thisList.pop(2)
print("pop method:", thisList)

copiedList = thisList.copy()
print("copy method:", copiedList)

thisList.clear()
print("clear method:", thisList)

# Dictionaries
thisDictionary = {"Key": "Value",
                  "RedID": 827578876, "Adress": "805 Palmetto Pl"}
print(thisDictionary, "is a type of", type(thisDictionary))
# Can also be written like this
abcNumConv = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4
}

# Accessing Dictionary
# Declaring Dictionarry
studentID = {"Dominic Parker": 748392853, "Kenneth Clayton": 82835023}
print("Original Dictionary:", studentID)
# Adding to Dictionary
studentID["Ryan Toy"] = 72739329
print("Adding Item:", studentID)
# Removing item
studentID.pop("Ryan Toy")
print("Removing item:", studentID)
# Removing last item
studentID.popitem()
print("Removing last item:", studentID)
# Adding all back
studentID["Kenneth Clayton"] = 82835023
studentID["Ryan Toy"] = 72739329
# Get value from key
kennethID = studentID.get("Kenneth Clayton")
print("Get value from key:", kennethID)

# If statements
num1 = 50
num2 = 25

if num1 > num2:
    print("Correct math!")

if num1 < num2:
    print("Less than!")
elif num1 > num2:
    print("Greater than!")
else:
    print("Neither!")

if num1 > 25 and num1 < 100:
    print("It is between 25 and 100!")

# Looping
for x in range(5):
    print(x)
print()
for x in range(3, 8):
    print(x)
print("Printing list of numbers:")
listOfNums = [1, 3, 2, 5, 3]
for i in listOfNums:
    print(i)
print("Practicing while loops")
a = 0
while a != 5:
    print(a)
    a = a + 1

# Importing Modules
x = math.pi
print(x)
