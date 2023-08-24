""" Thrillworks interview """
lista = [2, 3, 8, 4, 6, 7, 2, 9, 6, 8]
sum = 0
sumindexa = 0
sumindexb = 0
for i in range(0, len(lista)-1):
    # print(lista[i], lista[i+1])
    newsum = lista[i] + lista[i+1]
    # print('sum', newsum)
    for k in range(i+1, len(lista)):
        newsum = lista[i] + lista[k]
        # print('sum after k', newsum)
        if newsum > sum:
            sum = newsum
            sumindexa = i
            sumindexb = k
print(sum, sumindexa, sumindexb, lista[sumindexa], lista[sumindexb])


""" Assesment """
A = [1, 3, 6, 4, 1, 2]
def solution(A):
    A = [x for x in A if x > 0]  # Filter out negative and zero values, and duplicates
    A.sort()
    print(A)
    if not A or A[0] > 1:  # If there are no positive values, return 1
        return 1

    i = 1  # Find the smallest positive integer that is not in the array
    for x in A:
        if x == i:
            i += 1
        elif x > i:
            return i
    return i
# print(solution(A))


""" Assesment 2 """
S = "aabbb"
# S= "ba"
# S = "aaa"
# S = "b"
# S = "abba"
def solutionb(S):
    first_b = -1
    for i in range(len(S)):  # the first occurrence of 'b', if it exists
        if S[i] == 'b':
            first_b = i
            break
    if first_b == -1 or 'a' not in S[first_b:]:  # If 'b' doesn't exist, or if it occurs after the first 'a', return True
        return True
    return False  # Otherwise, 'b' occurs before 'a', so return False
# print(solutionb(S))




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

x = "hello"
# if condition returns False, AssertionError is raised:
assert x == "hello", "x should be 'hello'"
# assert x == "goodbye", "x should be 'hello'"
num2 = 3//2  # how many times 2 we have inside 3 = answer is 1
num3 = 3/2  # real division of numbers = answer is 1.5
print(num2, num3)

# module of number
n = int(input("Enter number: "))
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
print("The number:", rev)





