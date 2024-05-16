# break and continue statements are used to alter the flow of the loops
# break exits the loop entirely while continue skips the current iteration and proceeds to the next
# break statement is usually used inside decision-making statements such as if...else
# break statement with for loop
# terminate the loop when a condition is met
for i in range(5):
    if i ==3:
        break
    print(i)

# break statement with while loop
i = 0
while i < 5:
    if i == 3:
        break
    print(1)
    i += 1

# continue statement skips the current loop iteration, 
# moving the program's control flow to the next iteration
# continue statement with for loop
for i in range(5):
    if i == 3:
        continue
    print(i)

# contiue statement with while loop
# program to print odd numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)



# challenge
# write a function to calculate the sum of elements in a list that are greater than a given number.
# return the sum of the numbers greater than the given number.
# if numbers is [1, 2, 3, 4, 5] and n is 3, the return value should be 9 because 4 + 5 is 9.
def sum_greater_than(numbers, n):
    total = 0
    for num in numbers:
        if num > n:
            total += num
        return total
numbers = [1, 2, 3, 4, 5]
n = 3
result = sum_greater_than(numbers, n)
print(result)