# The if __name__ == '__main__': statement is a built-in mechanism that controls code execution. It determines 
# whether a Python file is being run directly as the main program or imported as a module into another script.

# How it works:
# Every time Python runs a file, it automatically creates a special hidden variable called __name__. The Python 
# interpreter assigns a value to this variable depending on how you executed the file:
# ---Running directly: If you execute the file yourself (e.g., typing python script.py in your terminal), 
#   Python assigns the string '__main__' to __name__.

# ---Importing as a module: If you import the file into another script (e.g., import script), Python assigns the 
#   actual filename (e.g., 'script') to __name__.

# ---The if __name__ == '__main__': line simply checks this variable. If it matches '__main__', the block of 
#   code inside it runs. If it does not match, the block is ignored.

# Why you need it:
# When you import a Python file, Python automatically executes all of its top-level code (code not inside a 
# function or class). Without this check, importing a file would instantly trigger any demonstration code, 
# prints, or main scripts written inside it


def main():
    print(f'file Name {__name__}')
if __name__ == '__main__':
    main()