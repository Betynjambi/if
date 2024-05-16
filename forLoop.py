# used to iterate over sequences such as lists, tuples, and strings
languages = ['Swift', 'Python', 'Go']
# access elements of the list one by one
for i in languages:
    print(i)

# loop through a string
language = 'Python'
# iterate over each character in language
for x in language:
    print(x)

# range() function returns a sequence of numbers
values = range(4)
# iterate from i = 0 to i = 3
for i in range (4):
    print(i)


# for loop else clause
# a for loop may include an optional else clause which runs after the loop finishes iterating
# else block will not execute if loop is stopped by a break statement
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")


# for loop without accessing items
# for loop repeats an action specified number of times
languages = ['Swift', 'Python', 'Go']
# looping to repeat an action without using the list elements
for language in languages:
    print('Hi')

# the underscore (_) signifies that a loop variable is a placeholder with its value intentionally ignored
# using _ indicates that the loop is there for repetition and not for accessing the elements
languages = ['Swift', 'Python', 'Go']
# using _ for placeholder variable
for _ in languages:
    print('Hi')


# nested for loops
# a for loop can contain another nested for loop. In each iteration of the outer loop, the inner loop executes its complete sequence of iterations
# outer loop
for i in range(2):
    #inner loop
    for j in range(2):
        print(f"i = {i}, j = {j}")


# challenge
# write a function to calculate the factorial of a number.
# the factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# for example, if n is 5, the return value should be 120 because 1*2*3*4*5 is 120
def factorial(n):
    # base case: factorial of 0 is 1
    if n == 0:  
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# test the function
print(factorial(5))  
