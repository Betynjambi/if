# while loop is used to repeat a block of code until a certain condition is met
number = 1
while number <= 3:
    print(number)
    number = number + 1

# calculate the sum of the numbers until user enters 0
number = int(input('Enter a number: '))
total = 0
# iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))
print('The sum is', total)

# infinite while loop
# while loop runs infinitely if its condition always evaluates to True, forming an infinite loop
#age = 32
# the test condition is always True
#while age > 18:
#    print('You can vote')
# above code is equivalent to:
#age = 32   
# the test condition is always True
#while True:
#   print('You can vote')


# while loop with break statement
# can terminate a while loop immediately using a break statement, bypassing the condition check
while True:
    user_input = input('Enter your name: ')
    # terminate the loop when user enters end
    if user_input == 'end':
        print(f'The loop is ended')
        break 
    print(f'Hi {user_input}')

# while loop with an else clause
# while loop can include an optional else clause, which executes when the loop condition becomes False
counter = 0
while counter < 2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')


# for loops vs while loops
# for loop usually used in the sequence when the number of iterations is known
for i in range(4): 
    print(i)

# while loop usually used when the numver of iterations is unknown
while True:
    user_input = input("Enter password: ")
    # terminate the loop when the user enters exit
    if user_input == 'exit':
        print(f'Status: Entry Rejected')
        break
    print(f'Status: Entry Allowed')



# challenge
# write a function to get the Fibonacci sequence less than a given number.
# the Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the previous two.
# for input 22, the return value should be [0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibonacci_less_than(limit):
    fib_sequence = [0, 1]  # initialize Fibonacci sequence with first two numbers
    while fib_sequence[-1] + fib_sequence[-2] < limit:  # continue until next Fibonacci number exceeds limit
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # adod next Fibonacci number
    return fib_sequence

# test the function with an example
result = fibonacci_less_than(22)
print(result)
