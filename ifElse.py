# any if statement executes a block of code only if the specified condition is met.
# if
number = 10
# check if the number is greater than 0
if number > 0:
    print('Number is positive')
print('This statement always executes')

# if...else
number = -5
if number > 0:
    print('Number is positive')
print("This statement always executes")

# an if statement can have an optional else clause
# the else statement executes if the condition in the if statement evaluates to false
number = 10
if number > 0:
    print('positive number')
else:
    print('negative number')
print('This statement always executes')

number = -5
if number > 0:
    print('positive number')
else:
    print('negative number')
print('This statement always executes')


#if...elif...else
# if...else statement picks between two code blocks. 
# for more choices, we use if...elif...else.
number = 0
if number > 0:
    print('Positive number')
elif number <0:
    print('Negative number')
else:
    print('Zero')
print('This statement always executes')


# nested if statements
# outer if statement
number = 5
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
    # outer else statement
else:
    print('Number is negative')

# outer if statement
number = -5
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
    # outer else statement
else:
    print('Number is negative')

# if shorthand - if statement can be simplified into a single line
number = 10
if number>0: print('Positive')
# the above can be written as:
number = 10
if number > 0:
    print('Positive')

# Python lacks a ternary operator, but if...else can mimic its function from other languages
grade = 40
if grade >= 50:
    result = 'pass'
else:
    result = 'fail'
print(result)
# the above can be written as:
grade = 40
result = 'pass' if number >= 50 else 'fail'
print(result)

# Logical operators like "and" and "or" can be utilized within an if statement
age = 35
salary = 6000
# add two conditions using and operator
if age >= 30 and salary >= 5000:
    print('Eligible for the premium membership')
else:
    print('Not eligible for the premium membership')


# a function to check whether a student passed or failed his/her exams
# assume the pass marks to be 50
# return Passed if the student scored more than 50. Otherwise, return Failed
def check_exam_score(score):
    pass_marks =50
    if score > pass_marks:
        return 'Passed'
    else:
        return 'Failed'
# passing the student's core as an argument
print(check_exam_score(60))
print(check_exam_score(40))
