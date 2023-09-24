


print('_____________________________________________________________________________________________________________________')


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



