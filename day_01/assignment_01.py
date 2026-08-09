'''
Name: Yuvraj Pavan Sabale
Batch: AIML
Day: 1(9th August 2026)
Assignment: 1
Description:

'''

# why python for AIML ? 
'''
Python is widely used for AI/ML because it is simple to learn, has a large number of libraries, and makes it easy to work with data and build models.
Some popular libraries are NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, and PyTorch. It also has a large community and lots of learning resources.

'''

# Datatypes in python 

num = 10
num2 = 10.5
num3 = 10 + 5j
str1 = "Hello world"
print(type(num))
print(type(num2))
print(type(num3))
print(type(str1))

my_dict = {'x': "abc", 'y': "def"}
print(type(my_dict))
print(my_dict["x"])

ls = [1,12.11,"xyz",3,4,5]

print(type(ls))
print(ls[1])


# slicing and indexing 

a = "Hello world this is python"
print(a[:7])
print(a[2:])
print(a[8:18])

# conditional statements problem formulation & also demonstrating for loop 

vowels = ["a", "e", "i", "o", "u"]
vcount = 0

text = input("Enter a string: ")

for i in text:
    if i in vowels:
        vcount+=1

print("Number of vowels in the string:", vcount)


# while loop demonstration

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# tuple and operations on a tuple 

numbers = (10, 20, 30, 40, 50)

print(numbers[0])      

# Slicing
print(numbers[1:4])   

# Length
print(len(numbers))    

# Checking an element
print(30 in numbers)   

# Count
print(numbers.count(20)) 

# Index
print(numbers.index(40))  

# Repetiing the tuple 2 times
print(numbers * 2)

