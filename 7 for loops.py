# --------------------------What is a for Loop -----------------------------
# A for loop in Python is a control flow statement used to iterate over a sequence (such as a list, tuple, string, 
# or range) or other iterable objects. Unlike for loops in languages like C or Java that use a counter and 
# condition, Python's for loop iterates directly over the items of the sequence in the order they appear. 
fruits = ['apple', 'banana', 'pawpaw', 'cashew']

for i in fruits:
    print(i)

#This will show all the numbers divisible by 3
for num in range(0, 100):
    if num % 3 == 0:
        print(num)

#FizzBuzz Challenge
for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)