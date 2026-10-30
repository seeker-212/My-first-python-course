# --------------------------- What are function ------------------------------
# Functions in Python are self-contained blocks of code designed to perform a specific task. 
# They allow developers to write code once and reuse it multiple times, promoting modularity and reducing errors.
# In python to set a function, you have to define it like this: def function, where as in js it's just: function
import time
choice = int(input('What number would you like to choose'))

def function(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
print('This program is about to run in 10 seconds')
time.sleep(10)
function(choice)

name = input('Please input you username here:')

def function(name):
    print('hello' + ' ' + name)
function(name)