'''  python Syntax  '''


def variables():
    name = "John"
    age = 25
    height = 1.75
    is_student = True

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

def email_send():
    import yagmail

    # Email
    email = 'alex27dz@gmail.com'
    subject = 'test1'
    body = 'hello world'
    pass_auth = 'yeqnnbfgkfetetcr'

    def send_email(email, subject, body):
        ya_email = yagmail.SMTP('alex27dz@gmail.com', pass_auth)
        ya_email.send(email, subject, body)
        print('email sent')

    send_email(email, subject, body)

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



















