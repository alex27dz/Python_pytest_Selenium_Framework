"""
Content:
* files
* For loops
* Data types
* leet code - sum of two
* working with str content inside files txt
* lists
* dictionaries
* number is prime
* files
* locate if name is correct in file
* assert vs if statement
* Asserts
* selenium
* strings
* requests get
* module of number
* Counters
* Deque
* Date
* Lambda
* Exceptions
"""

""" Thrillworks interview """
lista = [2, 3, 8, 4, 6, 7, 2, 9, 6, 8]
sum = 0
sumindexa = 0
sumindexb = 0

for i in range(0, len(lista)-1):
    newsum = lista[i] + lista[i+1]
    for k in range(i, len(lista)-1):
        newsum = lista[i] + lista[k]
        if (newsum > sum):
            sum = newsum
            sumindexa = i
            sumindexb = k

print(sumindexa, sumindexb)



try:
    print('hi')
except:
    try:
        print('bye')
    except:
        print('nothing')









# working with files

file = open('hello.txt', 'r')
content = file.read()
print(content)
file.close()

new_content = content.replace('alex', 'Bob')
file = open('hello.txt', 'w')
file.write(new_content)
file.close()

file = open('hello.txt', 'r')
content = file.read()
print(content)
file.close()


# files
import os
print(os.path.getsize('../alex.txt'))  # check file size




# For loops
for x in range(len(listofparamstwo)):
    print(listofparamstwo[x])

for x in range(0, 10):
    print(x)




# Data types
number = 1
dictionary = {
    "Car": "Black",
    'Keys': 'Blue'
}
boolean = True
setparams = {"one", "two", "three"}
listofparams = [1, 2, 3, 4]
listofparamstwo = ['alex', 'alex2', 'alex3']
string = 'hello world'
tupleone = (1, 2)
tupletwo = ('alex', 'god')
print(type(tupleone))
print(type(tupletwo))
print(type(setparams))
print(len(setparams))
print(len(listofparams))
print(listofparams[3])
print(listofparamstwo[1])
print(dictionary['Car'])
print(len(dictionary))



# leet code - sum of two
def twoSum(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[num] = i
    return None
# print(twoSum([2,7,11,15], 13))




# working with str content inside files txt
incorrect_name = 'Bob'
correct_name = 'Alex'
def correct_name_in_file(correct_name, incorrect_name):
    # opening the file and making a copy of the content into a string
    file = open('hello.txt', 'r')
    content = file.read()
    file.close()
    print(content)  # checking the string
    print(type(content))  # checking str type

    # content.find(incorrect_name)
    print(content.count(incorrect_name))
    if content.count(incorrect_name) == 0:
        print('name is correct')
    else:
        print('name is incorrect, replacing the name')
        file = open('hello.txt', 'w')
        newcontent = content.replace(incorrect_name, correct_name)
        print(newcontent)
        file.write(newcontent)
        file.close()
# correct_name_in_file(correct_name, incorrect_name)




# lists
nums = [1, 2, 3]
nums.index(1)  # returns index
nums.append(1)  # appends 1
nums.insert(0, 10)  # inserts 10 at 0th index
nums.remove(3)  # removes all instances of 3
# nums.copy(1)  # returns copy of the list
nums.count(1)  # returns no.of times '1' is present in the list
# nums.extend(someOtherList) # ...
nums.pop()  # pops last element [which element to pop can also be given as optional argument]
nums.reverse()  # reverses original list (nums in this case)
nums.sort()  # sorts list [does NOT return sorted list]
# Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
fruits.append("orange")
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]
fruits.extend(["grape", "kiwi"])
print(fruits)  # Output: ["apple", "banana", "cherry", "orange", "grape", "kiwi"]
fruits.insert(1, "pear")
print(fruits)  # Output: ["apple", "pear", "banana", "cherry", "orange", "grape", "kiwi"]
fruits.remove("cherry")
print(fruits)  # Output: ["apple", "pear", "banana", "orange", "grape", "kiwi"]
fruits.pop(3)
print(fruits)  # Output: ["apple", "pear", "banana", "grape", "kiwi"]
print(fruits.index("banana"))  # Output: 2
print(fruits.count("pear"))  # Output: 1
fruits.sort()
print(fruits)  # Output: ["apple", "banana", "grape", "kiwi", "pear"]
fruits.reverse()
print(fruits)  # Output: ["pear", "kiwi", "grape", "banana", "apple"]
mylist = [1,2,3,4,5,6,7,8,9]
new1list = mylist.copy()
new2list = mylist
new3list = mylist[:]
# print(new1list, new2list, new3list)
listofitems = [1,2,3,4,5,6,7,8,9]
list = ['alex', 'dani', 'BOB']
newlist = list.copy()
newnewlist = list[:]
# print(newlist)
# print(newnewlist)
# print(list)
string = "alex is the king"
newstring = string[:8]
# print(newstring)
# list append
def changelist(a):
    a.append('john')
    # print(a)
# changelist(list)  # print(list)



# dictionaries
dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(dict.keys())  # returns list of keys of dictionary
print(dict.values())  # returns list of values of dictionary
print(dict.get('a'))  # returns value for any corresponding key
print(dict.items())  # returns [('a',1),('b',2),('c',3)]
dict.copy()  # returns copy of the dictionary
# NOTE : items() Returns view object that will be updated with any future changes to dict
# dict.pop('KEY')  # pops key-value pair with that key
dict.popitem()  # removes most recent pair added
dict.setdefault('KEY', 2)  # returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd argument's default is None.
dict.update({'KEY': 'VALUE'})  # inserts pair in dictionary if not present, if present, corresponding value is overriden (not key)
# defaultdict ensures that if any element is accessed that is not present in the dictionary
# it will be created and error will not be thrown (which happens in normal dictionary)
# Also, the new element created will be of argument type, for example in the below line
# an element of type 'list' will be made for a Key that does not exist
# myDictionary = defaultdict(list)
dict = {
    'key': 'value',
    'name': 'alex'
}
fruits = {"apple": 1, "banana": 2, "cherry": 3}
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




# number is prime
def numisprime(num):
    print(num, 'number')
    if num <= 1:
        return False, "number is not prime"
    else:
        flag = 1
        for i in range(2, num):
            print(i, 'i parameter of the for loop')
            if num % i == 0:
                return False, "number is not prime"
            else:
                flag += 1
                print(flag, ' flag indicates if the number devided by something')
        if flag == (num - 1):
            return True, 'number is prime!'
# print(numisprime(5))




# files - open file , check content , change content , save file, close
import argparse
import os
# file object = open(file_name [, access_mode][, buffering])
f = open('dog_breeds.txt')
print(f.readlines())  # Returns a list object!
print(type(f))
# Close opened file
f.close()
# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()

with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')

with open('dog_breeds.txt', 'r') as reader:
    print(reader.read())

d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

# Writing
with open('dog_breeds_reversed.txt', 'w') as writer:
    writer.write('Boom')

file = 'hello.txt'
oldn = 'Bob'
newname = 'Alex'




# locate if name is correct in file
def locatednameinfile(filename, oldname, name):
    file = open(filename, 'r')
    content = file.read()
    print(content)
    print(type(content))
    if name in content:
        return True, 'name is located in content'
    else:
        fixedcontent = content.replace(newname, oldname)
        file = open(filename, 'w')
        file.write(fixedcontent)
        file.close()
        return False, 'name was not located in the file, content of the file updated'
# locatednameinfile(file, oldn, newname)  # print(locatednameinfile(file, oldn, newname))




# assert vs if statement
def dividee(a, b):
    if b == 0:
        print("if statement - Error: division by zero")
        return False
    else:
        return a / b
# result1 = dividee(4, 2)  # result = 2.0
# result2 = dividee(4, 0)  # prints "Error: division by zero" and returns None




# assert Example using  statement
def divide(a, b):
    assert b != 0, "assert - Error: division by zero"
    return a / b
# result3 = divide(4, 2)  # result = 2.0
# result4 = divide(4, 0)  # raises AssertionError with message "Error: division by zero"
x = "hello"
# if condition returns False, AssertionError is raised:
assert x == "hello", "x should be 'hello'"
# assert x == "goodbye", "x should be 'hello'"
num2 = 3//2  # how many times 2 we have inside 3 = answer is 1
num3 = 3/2  # real division of numbers = answer is 1.5
print(num2, num3)



# selenium open webpage
import time
from selenium import webdriver
def open_web_page():
    chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://www.google.com/')
    time.sleep(5)
# open_web_page()




# strings
# The split() - method breaks up a string at the specified separator and returns a list of strings.
text = 'Python is a fun programming language'
print(text.split(' '))  # split the text from space
s = "abcd"  # convert string to list
s = list(s)
# Output: ['Python', 'is', 'a', 'fun', 'programming', 'language']
# The count() - method returns the number of occurrences of a substring in the given string.
message = 'python is popular programming language'
print('Number of occurrence of p:', message.count('p')) # Counting P in string - Output: Number of occurrence of p: 4
# The isnumeric() - method returns True if all characters in a string are numeric characters. If not, it returns False.
snum = '1242323'
print(snum.isnumeric())  # Output: True
# The find() - method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
# check the index of 'fun'
print(message.find('fun'))  # Output: 12
# The isalnum() - method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
name = "M3onica Gell22er "
print(name.isalnum())  # Output : False
# The isalpha() - method returns True if all characters in the string are alphabets. If not, it returns False
name = "Monica"
print(name.isalpha())  # output true
string.upper() #he upper() method converts all lowercase characters in a string into uppercase characters and returns it.
string.lower() #The lower() method converts all uppercase characters in a string into lowercase characters and returns it.
str1 = 'string'
str2 = str1[0: 3]
str3 = str1[:]
print(str2)
print(str3)
# we can't delete or change a string
mystring = 'Ford is the best Ford company'
# print(mystring)
newstring = mystring[0:40]
# print(newstring)
new5string = mystring.replace('Ford', 'Alex')
# print(new5string)
newstring = mystring[:]
new2string = mystring
# print(newstring,new2string)
# print(mystring.find('aaaaa'))




# requests get
import requests
def get_request():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data = response.json()
    print(type(data))
    print(data)
    print(data['userId'])
    print(data['title'])
# get_request()




# module of number
n = int(input("Enter number: "))
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
print("The number:", rev)




# Counters - counters elements in the container, string, list,
import collections
from collections import Counter  # (capital 'C') - can also be used as 'collections.Counter()' in code
list1 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
# Initialization
Counter(list1) # => Counter({'x': 4, 'y': 2, 'z': 2})
Counter("Welcome to Guru99 Tutorials!")  # => Counter({'o': 3, ' ': 3, 'u': 3, 'e': 2.....})
# Updating
counterObject = collections.Counter(list1)
print(counterObject)
# counterObject.keys() = [ 'x' , 'y' , 'z' ]
most_common_element = counterObject.most_common(1)  # [('x', 4)]
print(most_common_element)
counterObject.update("some string")  # => Counter({'o': 3, 'u': 3, 'e': 2, 's': 2})
counterObject['s'] += 1  # Increase/Decrease frequency




# Deque, has the feature of adding and removing elements from either end.
from collections import deque
queue = deque(['name', 'age', 'DOB'])
queue.append("append_from_right")  # Append from right
queue.pop()  # Pop from right
queue.appendleft("fromLeft")  # Append from left
queue.popleft()  # Pop from left
# queue.index(element, begin_index, end_index) # Returns first index of element b/w the 2 indices.
# queue.insert(index,element)
# queue.remove()  # removes first occurrance
# queue.count()  # obvious
queue.reverse()  # reverses order of queue elements




# Date
from datetime import datetime
date = datetime.now()
print(date)
date_string = "27 June, 2023"
print(datetime.strptime(date_string, "%d %B, %Y"))
date_new = datetime(2019, 11, 27, 11, 27, 22)




# Lambda function multiplies all the items in the list
my_list = [1, 2, 3, 4]
my_list = list(map(lambda x: 2*x, my_list))
new_list = list(map(lambda x: 3*x, my_list))
print(my_list)
print(new_list)




# Exceptions
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
