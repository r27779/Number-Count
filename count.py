"""
Number Counter Program

Program asks for 3 inputs from user

Start value, end value and step value

Once values are entered sequence will print

"""
print('\nWelcome to the number counting program.\n')
print('Please follow the prompts to print a range of numbers.\n')
while True:
    START = input('Enter a start value (Default:0): ')
    if START == "":
        START = 0
        break
    elif not START.isdigit():
        print('Not a number.  Please re-enter after prompt')
    else:
        START = int(START)
        break
while True:
    END = input('Enter an end value: ')
    if END == "":
        print('You must enter a number.')
    elif not END.isdigit():
        print('Not a number.  Please re-enter after prompt')
    elif END == '0':
        print('End Value must be greater than 0.  Please re-enter after prompt.')
    else:
        END = int(END)
        break
while True:
    STEP = input('Enter a step value (Default:1):')
    if STEP == "":
        STEP = 1
        break
    elif not STEP.isdigit():
        print('Not a number. Please re-enter afer prompt.')
    elif STEP == "0":
        print('You must enter a value greater than 0.  Please re-enter afer prompt.')
    else:
        STEP = int(STEP)
        break
print(list(range(START, END+1, STEP)))
