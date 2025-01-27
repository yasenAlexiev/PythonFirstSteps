import math
import string

# Define a function called myfunc that takes in a string,
# and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
def myfunc(mystring):
    index = 0
    result = ''
    for letter in mystring:
        if index % 2 == 0:
            result = result + letter.lower()
        else:
            result = result + letter.upper()
        index += 1

    return result


print(myfunc('Anthropomorphism'))


##########################
# HOMEWORK

# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return 4 / 3 * math.pi * rad ** 3


print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(f'{num} is in the range between {low} and {high}')


ran_check(5, 2, 7)


def ran_bool(num, low, high):
    return num in range(low, high + 1)


print(ran_bool(3, 1, 10))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    low_count = 0
    upper_count = 0
    for letter in s:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            low_count += 1

    print(f'No. of Upper case characters : {upper_count}')
    print(f'No. of Lower case characters : {low_count}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num

    return result


print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    return s == s[::-1]

print(palindrome('411114'))


# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
def ispangram(str1, alphabet=string.ascii_lowercase):
    buff = list(set(str1.replace(' ', '').lower()))
    buff.sort()
    return ''.join(buff) == alphabet


print(ispangram("The quick brown fox jumps over the lazy dog"))