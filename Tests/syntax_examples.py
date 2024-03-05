def variables():
    name = 'alex'
    age = 15
    print(type(age), type(name))
    is_flag = True
    same_flag = False
    print(type(is_flag), type(same_flag))
def strings():
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
def lists():
    lista = [5, 2, 3]
    print(lista)
    len(lista)  # Returns the number of elements in the list.
    listb = ['alex', 'bob', 'john']
    new_list = listb[0:3]  # slicing
    print(new_list)
    listc = ['a', 'b', 'c', 'd']
    print(listc)
    item = 1
    index = 1
    listb.append(item)  # Adds an element to the end of the list.
    listb.insert(index, item)  # Inserts an element at a specific index in the list.
    listb.remove(item)  # Removes the first occurrence of an element from the list.
    listb.pop(index)  # Removes and returns the element at a specific index in the list.
    list.sort(lista)  # Sorts the elements of the list in ascending order.
    print(lista)
    listb.reverse()  # Reverses the order of the elements in the list.
    listb.index(item)  # Returns the index of the first occurrence of an element in the list.
    listb.count(item)  # Returns the number of times an element appears in the list.
    listb.copy()  # Returns a shallow copy of the list.
    listb.clear()  # Removes all elements from the list
    iterable = 'a'
    listb.extend(iterable)  # Appends the elements of an iterable to the end of the list.
def dictionary():
    fruits = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print(fruits)
    print(fruits["apple"])  # printing value of apple key
    print(len(fruits))  # Output: 3
    print(fruits.keys())  # Output: dict_keys(['apple', 'banana', 'cherry'])
    print(fruits.values())  # Output: dict_values([1, 2, 3])
    print(fruits.items())  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])
    print(fruits.get("apple", 0))  # Output: 1
    print(fruits.get("orange", 0))  # Output: 0
    removed_value = fruits.pop("banana", 0)
    print(removed_value)  # Output: 2
    print(fruits)  # Output: {'apple': 1, 'cherry': 3}
    key, value = fruits.popitem()
    print(key, value)  # Output: ('cherry', 3)
    print(fruits)  # Output: {'apple': 1}
    fruits.update({"orange": 4, "grape": 5})
    print(fruits)  # Output: {'apple': 1, 'orange': 4, 'grape': 5}
    fruits.clear()
    print(fruits)  # Output: {}
    person = {"name": "Alice", "age": 25, "city": "New York"}
    print(person["name"])

    dicty = {
        'Key1': 'value1',
        'Key2': 'value2',
        'Key3': 'value3'
    }

    print(type(dicty))
    print(dicty)
    print(dicty['Key1'])

    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Key to search for
    key_to_find = 'alex'

    # Initialize a variable to store the found key
    found_key = None

    # Iterate through the dictionary
    for key in my_dict:
        if key == key_to_find:
            found_key = key
            break  # Stop searching once the key is found

    if found_key is not None:
        print(f"Key '{key_to_find}' is present in the dictionary")
    else:
        print(f"Key '{key_to_find}' is not present in the dictionary")

    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Value to search for
    value_to_find = 'John'

    # Initialize a variable to store the found key
    found_key = None

    # Iterate through the dictionary
    for key, value in my_dict.items():
        if value == value_to_find:
            found_key = key
            break  # Stop searching once the value is found

    if found_key is not None:
        print(f"Key for value '{value_to_find}' is '{found_key}'")
    else:
        print(f"Value '{value_to_find}' not found in the dictionary")

    print(my_dict.items())
    print(len(my_dict))
def gmail_send():
    import yagmail  # working with yaGmail

    email = 'alex27dz@gmail.com'
    resciever = 'alex31mann@gmail.com'

    subject = 'Hi its a test'
    body = 'Life is perfect'
    auth = 'yeqnnbfgkfetetcr'

    def send_gmail(email, resciever, subject, body):
        ya_email = yagmail.SMTP(email, auth)  # sender and authentication
        ya_email.send(resciever, subject, body)  # resciever, subject title , body
        print('Email sent')

    send_gmail(email, resciever, subject, body)
def linux_bash_commands():
    '''
    Bash and terminal commands in Linux:
    ls: List files and directories in the current directory.
    cd: Change the current directory.
    pwd: Print the working directory (current directory).
    mkdir: Create a new directory.
    rm: Remove/delete files or directories.
    cp: Copy files or directories.
    mv: Move or rename files or directories.
    touch: Create an empty file or update the access/modification time of a file.
    '''

    '''
    cat: Concatenate and display the content of files.
    more: Display file content one screen at a time.
    less: View file content with backward navigation support.
    head: Display the beginning of a file (default: first 10 lines).
    tail: Display the end of a file (default: last 10 lines).
    grep: Search for a specific pattern in files.
    find: Search for files and directories in a directory hierarchy.
    ps: Show information about running processes.
    kill: Terminate processes using their process ID (PID).
    top: Display system monitoring information and current processes.
    df: Show disk space usage for file systems.
    du: Estimate file and directory space usage.
    chmod: Change file permissions.
    chown: Change file ownership.
    tar: Create or extract tar archives.
    ssh: Connect to a remote server using SSH.
    scp: Securely copy files between local and remote systems over SSH.
    ping: Send ICMP echo requests to a host.
    wget: Download files from the internet.
    curl: Transfer data with URLs.
    history: Display the command history.
    man: Display the manual page of a command.
    '''
def os_library_commands():
    # OS - operating systems library

    import os
    # os.rename('old_file.txt', 'new_file.txt')  # Rename a file
    # os.remove('file.txt')  # Delete a file
    # os.mkdir('new_directory')  # Create a directory
    # os.rmdir('existing_directory')  # Remove a directory
    # current_dir = os.getcwd()  # Get the current working directory
    # os.chdir('new_directory')  # Change the current working directory
    abs_path = os.path.abspath('data.txt')  # Get the absolute path
    size = os.path.getsize('new_file.txt')
    path = os.path.exists('file.txt')
    path2 = os.path.isfile('file.txt')
    path3 = os.path.isdir('directory')
    path4 = os.path.join('folder', 'file.txt')
def built_in_funcs():
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
def if_statement():
    # if statements
    age = 19
    if age > 18:
        print('adult')
    else:
        print('child')
def for_while_loops():
    # For Loops
    for i in range(1, 10):
        print(i, 'for loop')

    name = 'alex'
    for i in name:
        print(i, 'i in string')
    i = 0

    while i < 10:
        print(i, 'while loop')
        i += 1
def break_continue():
    # Control Flow
    for i in range(1, 10):
        if i == 5:
            break
        print(i, 'control flow')
    for i in range(1, 10):
        if i == 5:
            continue
        print(i)
def function_example():
    print('doing something')
    return True
def yield_functionality():
    # Yield - temporarily suspends execution and returns the yielded value (using generator)
    # Instead of using return, we use the yield keyword. This turns the function into a generator,
    # allowing it to "pause" its execution state and yield each line of the file one by one as you iterate over it.
    # This approach is useful when dealing with large files or when you want to process data lazily,
    # one piece at a time, without loading everything into memory

    real_numbers_list = [1, 2, 3, 4, 5]

    def number_generator(number_list):  # yield the numbers in the list
        for num in number_list:
            print(num)
            yield num


    # (must) creating generator - combining the list with the functions that yield
    gen = number_generator(real_numbers_list)

    # printing back the yield numbers using generator
    for item in gen:
        print(item)
def fibonacci_list_append(n):
    if n<=0:
        print('no items in the list')
    else:
        if n==1:
            print('one element')
            return [0]
        else:
            if n==2:
                print('two elements')
            else:
                if n>=3:
                    print('fibonacci list of ', n, ' elements')
                    fibo_list = [0,1]
                    for i in range(2,n):
                        print('element num', i)
                        new_item = fibo_list[i-1] + fibo_list[i-2]
                        fibo_list.append(new_item)
                    print(fibo_list)
                    return fibo_list

    # fibo = fibonacci_list_append(10)
    # print(fibo)
    # print(type(fibo))
def map_function():
    # combining a function with a list or numbers to perform an action
    # map (function, list_of_numbers)
    # running the function for all list_of_numbers

    def square(x):    # Define a function to square a number
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)  # Use map() to apply the square function to each number in the list
    print(type(squared_numbers))
    squared_numbers = list(squared_numbers)  # Convert the map object to a list
    print(squared_numbers)
def lambda_function():
    # Lambda function - used for short, one-time operations
    # lambda     arguments : expression
    # lambda  [parameters] : [actions]

    # arithmetic
    add = lambda x, y: x + y  # lambda function
    multiply = lambda x, y: x * y  # lambda function
    print(add(5, 6))
    print(multiply(5, 6))

    # list functions
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x ** 2 for x in numbers]
    print(squared_numbers)

    # sorting inside a list of dictionaries
    students = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 28}]
    print(students)
    print(type(students.sort(key=lambda student: student['age'])))
    print(students)

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
def files_read():
    # reading from a file
    file = open('text_example_file.txt', 'r')
    content = file.read()
    print(content)
    file.close()
def files_write_create():
    # writing to a file / creating a file
    new_content = 'Hi Im Alex and this is a new content'
    file = open('new_file.txt', 'w')
    file.write(new_content)
    file.close()
    # reading from a file
    file = open('new_file.txt', 'r')
    content = file.read()
    print(content)
    file.close()
def files_appending():
    file = open('data.txt', 'a')  # appending data into a file
    file.write('\nAppending new data.')
    file.close()
def try_except():
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
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def car_color(self):
        print(self.color)

    def car_brand(self):
        print(self.brand)
def car_class():
    bmw = Car('Black', 'BMW')
    bmw.car_color()
    bmw.car_brand()
def class_inheritance():
    class ParentClass:
        def parent_method(self):
            print("This is the parent method")

    class ChildClass(ParentClass):  # attributing parent class
        def child_method(self):
            super().parent_method()  # Call the parent method
            print("This is the child method")

    child_instance = ChildClass()
    child_instance.child_method()
def date_time():
    # Date
    from datetime import datetime
    date = datetime.now()  # 1
    date_string = "27 June, 2023"  # 2
    date_new = datetime(2019, 11, 27, 11, 27, 22)  # 3
    print(date, 'option 1')
    print(datetime.strptime(date_string, "%d %B, %Y"), 'option 2')
    print(date_new, 'option 3')
def logging_funcs():
    import logging
    logging.basicConfig(filename='new_file.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logging.debug('hello')

    # reading the logs file
    file = open('new_file.txt', 'r')
    print(file.read())
    file.close()
def http_requests():
    '''
    Requests - making HTTP request to the server and handling response
    get request - retrieve data from server
    post request - send data to server
    response.status_code
    content = response.text
    content = response.json()
    '''

    import requests

    # Making a GET request to retrieve data from a URL
    url = 'https://example.com'
    response = requests.get(url)
    statuscode = response.status_code  # Check the status code of the response
    content = response.text

    # Making a POST request with data
    post_url = 'https://example.com/post'
    data = {'key': 'value'}
    post_response = requests.post(post_url, data=data)
    post_statuscode = post_response.status_code
    post_content = post_response.text

    # Handling JSON data in a response
    json_url = 'https://api.example.com/data.json'
    json_response = requests.get(json_url)
    json_statuscode = json_response.status_code
    json_data = json_response.json()
def seleniumopenweb():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    driver.maximize_window()
    time.sleep(2)






























