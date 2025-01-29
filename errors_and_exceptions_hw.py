import unittest

class TestText(unittest.TestCase):

    def test(self):
        pass

# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("You can't squared strings!")
finally:
    print("Do the final print")

# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError:
    print("You can't divided by 0!!!")
finally:
    print("All Done")


# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except,
# else block to account for incorrect inputs.

def ask():
    while True:
        try:
            number = int(input("Please enter a number: "))

        except ValueError:
            print("this is not a number")
        else:
            print("Thank you")
            break

    print(f"Your number squared is: {number ** 2}")


ask()
