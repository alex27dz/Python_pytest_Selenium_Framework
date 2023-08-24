# Variables and Data Types
name = "John"
age = 25
height = 1.75
is_student = True
# print(type(is_student))
# print(is_student)
print('_____________________________________________________________________________________________________________________')

# Built-in functions
my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3, 4, 5]
is_list1 = isinstance(my_list1, list)
is_list2 = isinstance(my_list2, list)
print(is_list1)  # Output: True
print(is_list2)  # Output: True
# list()
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]
# abs()
number = -10
absolute_value = abs(number)
print(absolute_value)  # Output: 10
# bin()
number = 10
binary_string = bin(number)
print(binary_string)  # Output: '0b1010'
# exec()  - executing the code inside the parameter as string
code = """
for i in range(5):
    print(i)
"""
exec(code)  # Output:# 0# 1# 2# 3# 4
# float()
number = '3.14'
float_number = float(number)
print(float_number)  # Output: 3.14
# format()
name = "Alice"
age = 25
formatted_string = "My name is {} and I'm {} years old".format(name, age)
print(formatted_string)  # Output: My name is Alice, and I'm 25 years old
# globals()
global_variable = 10
global_variables = globals()
print(global_variables['global_variable'])  # Output: 10
# hex()
number = 255
hex_string = hex(number)
print(hex_string)  # Output: '0xff'
# id()
my_list = [1, 2, 3]
list_id = id(my_list)
print(list_id)  # Output: [a unique identifier]
# input()
# name = input("Enter your name: ")
print("Hello, " + name)  # Output: Hello, [name]
# int()
number = '10'
integer_number = int(number)
print(integer_number)  # Output: 10
# len()
my_list2 = [1, 2, 3, 4, 5]
length = len(my_list2)
print(length)  # Output: 5
# list()
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]
# max()
numbers = [4, 2, 7, 1, 5]
max_number = max(numbers)
print(max_number)  # Output: 7
# min()
numbers = [4, 2, 7, 1, 5]
min_number = min(numbers)
print(min_number)  # Output: 1
# open()
file = open("data.txt", "r")
contents = file.read()
print(contents)
file.close()
# reversed()
my_list = [1, 2, 3]
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [3, 2, 1]
# round()
value = 3.14159
rounded_value = round(value, 2)
print(rounded_value)  # Output: 3.14
# slice()
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]
print(sliced_list)  # Output: [2, 3, 4]
# sorted()
numbers = [4, 2, 7, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 4, 5, 7]
# str()
number = 10
string_number = str(number)
print(string_number)  # Output: '10'
# sum()
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(total)  # Output: 15
# tuple()
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)
# type()
my_object = object()
print(type(my_object))  # Output: <class 'object'>
# zip()
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
zipped = zip(numbers, letters)
for item in zipped:
    print(item)  # Output: # (1, 'A')# (2, 'B')# (3, 'C')

print('_____________________________________________________________________________________________________________________')
# Lists
list = [1, 2, 3]
listb = ['alex', 'bob', 'john']
# slicing
list = ['a', 'b', 'c', 'd']
new_list = list[0:3]
print(new_list)
print(list)
item = 1
index = 1
iterable = 'a'
len(list)  # Returns the number of elements in the list.
listb.append(item)  # Adds an element to the end of the list.
listb.insert(index, item)  # Inserts an element at a specific index in the list.
listb.remove(item)  # Removes the first occurrence of an element from the list.
listb.pop(index)  # Removes and returns the element at a specific index in the list.
list.sort()  # Sorts the elements of the list in ascending order.
listb.reverse()  # Reverses the order of the elements in the list.
listb.index(item)  # Returns the index of the first occurrence of an element in the list.
listb.count(item)  # Returns the number of times an element appears in the list.
listb.copy()  # Returns a shallow copy of the list.
listb.clear()  # Removes all elements from the list
listb.extend(iterable)  # Appends the elements of an iterable to the end of the list.
print('_____________________________________________________________________________________________________________________')

# Strings
string = 'example'
substring = 'example2'
old = 'e'
new = 'a'
separator = ','
print(string[0])  # String indexing
print(string[1:4])  # String Slicing
len(string)  # Returns the length of the string.
string.lower()  # Returns the lowercase version of the string.string.upper(): Returns the uppercase version of the string.
string.strip()  # Removes leading and trailing whitespace from the string.
string.replace(old, new)  # Replaces all occurrences of old in the string with new.
string.split(separator)  # Splits the string into a list of substrings based on the separator.
string.startswith(substring)  # Returns True if the string starts with the specified substring.
string.endswith(substring)  # Returns True if the string ends with the specified substring.
string.count(substring)  # Returns the number of times substring appears in the string.
string.find(substring)  # Returns the index of the first occurrence of substring in the string.
string.isnumeric()  # Returns True if the string consists of only numeric characters.
string.isalpha()  # Returns True if the string consists of only alphabetic characters.
string.isalnum()  # Returns True if the string consists of only alphanumeric characters.
print('_____________________________________________________________________________________________________________________')

# Dictionary        { "key", "Value" }
fruits = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}
print(fruits)
print(fruits["apple"])  # printing value of apple key
print(len(fruits))                # Output: 3
print(fruits.keys())              # Output: dict_keys(['apple', 'banana', 'cherry'])
print(fruits.values())            # Output: dict_values([1, 2, 3])
print(fruits.items())             # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])
print(fruits.get("apple", 0))     # Output: 1
print(fruits.get("orange", 0))    # Output: 0
removed_value = fruits.pop("banana", 0)
print(removed_value)              # Output: 2
print(fruits)                     # Output: {'apple': 1, 'cherry': 3}
key, value = fruits.popitem()
print(key, value)                 # Output: ('cherry', 3)
print(fruits)                     # Output: {'apple': 1}
fruits.update({"orange": 4, "grape": 5})
print(fruits)                     # Output: {'apple': 1, 'orange': 4, 'grape': 5}
fruits.clear()
print(fruits)                     # Output: {}
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])
print('_____________________________________________________________________________________________________________________')

# if statements
if age > 18:
    print('adult')
else:
    print('child')
print('_____________________________________________________________________________________________________________________')

# For Loops
for i in range(1, 10):
    print(i, 'for loop')
for i in name:
    print(i, 'i in string')
i = 0
while i < 10:
    print(i, 'while loop')
    i += 1
print('_____________________________________________________________________________________________________________________')

# Control Flow
for i in range(1, 10):
    if i == 5:
        break
    print(i, 'control flow')
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
def some_function():
    pass
print('_____________________________________________________________________________________________________________________')

# Functions
def something(myname):
    return myname
result = something(name)
# print('my name', result)
print('_____________________________________________________________________________________________________________________')

# yield
#      Temporarily suspends execution and returns the yielded value
#      The function's state is saved, allowing it to resume from where it left off the next time it is called
#      It's important to note that generator functions don't execute the entire function body at once;
#      they only execute until the next yield statement and then pause until the next iteration.
#      This makes them efficient for working with large datasets or performing iterative computations.
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
# Using the generator function
counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Output: 4
print(next(counter))  # Output: 5
# using next to execute the function from yield to the next yield

# reading lines from a txt file using yield
def read_lines(filename):
    file = open(filename, 'r')
    for line in file:
        yield line
lines_gen = read_lines('data.txt')
for line in lines_gen:
    print(line)
def filter_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            yield num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Using the generator function
odd_gen = filter_odd(numbers)
for num in odd_gen:
    print(num, 'odd')  # Output: 1 3 5 7 9
print('_____________________________________________________________________________________________________________________')

# Fibonacci
#      basically it is a sum of two numbers, every next element in the list will be the sum of the two previous elements using append
#      [0,1] -> next element will be 1, because [0] + [1] = 1, next element will be 2 because [1] + [1] = 2 -> new list [0,1,1,2] ....... using append
def fibonacci(n):
    if n <= 0:
        return []  # empty list
    elif n == 1:
        return [0]  # one element
    elif n == 2:
        return [0, 1]  # two elements
    else:  # if we have more than 3 numbers to count we will have to add into our list
        fib_sequence = [0, 1]  # start point
        for i in range(2, n):
            next_number = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_number)
        return fib_sequence
fib_sequence = fibonacci(10)
print(fib_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print('_____________________________________________________________________________________________________________________')

# Lambda
#      Short one-time-use function
#      or when you want to pass a function to another function used mostly with numbers
#      lambda [parameters]:[actions]
add_func = lambda x, y: x + y
print(add_func(5, 6), 'lambda')
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
print('_____________________________________________________________________________________________________________________')

# working with files
file = open('new_file.txt', 'w')  # creating new file
file.write('This is a new file.')  # Write content to the file
file.close()  # Close the file

file = open('data.txt', 'r')  # read from a file
content = file.read()
print(content)
file.close()

new_content = 'alex'  # write into a file
file = open('data.txt', 'w')
file.write(new_content)
file.close()

file = open('data.txt', 'a')  # appending data into a file
file.write('\nAppending new data.')
file.close()
file = open('data.txt', 'r')  # Reading a File Line by Line
for line in file:
    print(line)
file.close()

# working with strings inside files txt
incorrect_name = 'Bob'
correct_name = 'Alex'
def correct_name_in_file(cor_name, incor_name):
    file = open('hello.txt', 'r')  # open file copy into a string
    content = file.read()
    file.close()
    print(content, type(content))  # checking type
    print(content.count(incor_name))
    if content.count(incor_name) == 0:
        print('name is correct')
    else:
        print('name is incorrect, replacing the name')
        file = open('hello.txt', 'w')  # open file with writing option
        newcontent = content.replace(incor_name, cor_name)
        print(newcontent)
        file.write(newcontent)  # writing into the file
        file.close()
correct_name_in_file(correct_name, incorrect_name)
print('_____________________________________________________________________________________________________________________')

# OS - operating systems library
import os
# os.rename('old_file.txt', 'new_file.txt')  # Rename a file
# os.remove('file.txt')  # Delete a file
# os.mkdir('new_directory')  # Create a directory
# os.rmdir('existing_directory')  # Remove a directory
# current_dir = os.getcwd()  # Get the current working directory
# print("Current Directory:", current_dir)
# os.chdir('new_directory')  # Change the current working directory
# print("Updated Directory:", os.getcwd())
if os.path.exists('file.txt'):  # Check if a file or directory exists
    print("The file exists.")
if os.path.isfile('file.txt'):  # Check if a path refers to a file
    print("It's a file.")
if os.path.isdir('directory'):  # Check if a path refers to a directory
    print("It's a directory.")
# path = os.path.join('folder', 'file.txt')  # Join paths
# print("Joined Path:", path)
file_size = os.path.getsize('data.txt')  # Get the size of a file
print("File Size (bytes):", file_size)
abs_path = os.path.abspath('data.txt')  # Get the absolute path
print("Absolute Path:", abs_path)
# ________________________________________________________________________________

# try except
try:
    print('hi')
except:
    try:
        print('bye')
    except:
        print('nothing')
# Exceptions
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
# ________________________________________________________________________________

# Classes             Object-Oriented Programming
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def print_mark(self):
        print('model is', self.model)
        print('color is:', self.color)
mazda = Car('mx5', 'black')
mazda.print_mark()
# ________________________________________________________________________________

# Date
from datetime import datetime
date = datetime.now()  # 1
date_string = "27 June, 2023"  # 2
date_new = datetime(2019, 11, 27, 11, 27, 22)  # 3
print(date, 'option 1')
print(datetime.strptime(date_string, "%d %B, %Y"), 'option 2')
print(date_new, 'option 3')
# ________________________________________________________________________________

# Asserts - pytest












# ________________________________________________________________________________

# @pytest.fixtures




# ________________________________________________________________________________

# selenium open webpage


# ________________________________________________________________________________

# requests get
# import requests
# def get_request():
    # response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    # data = response.json()
    # print(type(data))
    # print(data)
    # print(data['userId'])
    # print(data['title'])
# get_request()
# ________________________________________________________________________________



