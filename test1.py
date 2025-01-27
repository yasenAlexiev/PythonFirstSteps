# Use for, .split(), and if to create a Statement that will print out words that start with 's':
def task1():
    st = 'Print only the words that start with s in this sentence'
    for word in st.split():
        if word[0].lower() == 's':
            print(word)


# Use range() to print all the even numbers from 0 to 10.
def task2():
    print(list(range(0, 11, 2)))


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
def task3():
    print([num for num in range(1, 51) if num % 3 == 0])


# Go through the string below and if the length of a word is even print "even!"
def task4():
    st = 'Print every word in this sentence that has an even number of letters'
    for word in st.split():
        if len(word) % 2 == 0:
            print('even!')


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
def task5():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fuzz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)


# Use List Comprehension to create a list of the first letters of every word in the string below:
def task6():
    st = 'Create a list of the first letters of every word in this string'
    print([word[0] for word in st.split()])


task1()
task2()
task3()
task4()
task5()
task6()
