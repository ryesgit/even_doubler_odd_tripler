'''
filename: edot.py

Takes in a file input, distinguishes odd from even, and then double or triple them.

1. Take a file input
2. Iterate through all the numbers from file input
    - If even, then double and append to even.txt file
    - If odd, then triple and append to odd.txt file
3. Remember to close the txt file! (Use with operator for a foolproof execution!)

'''
from math import pow

first_odd = False
first_even = False

def edot(file_path):

    # Look for file input (integers.txt by default) file
    file_path = 'integers.txt' if file_path == '' else file_path
    try:
        with open(file_path, 'r') as numbers:
            # Iterate through every number from numbers.txt
            numbers = numbers.readlines()

            for number in numbers:
                # If number is even
                if(int(number.strip()) % 2 == 0):
                    store_to_file(int(number), 'even')
                # If number is odd
                else:
                    store_to_file(int(number), 'odd')

    except FileNotFoundError:
        raise f'File {file_path} does not exist.'

def store_to_file(number, mode):

    global first_odd, first_even

    # Determine exponent based on mode
    exponent = 2 if mode == 'even' else 3

    # If number is first on list, create a new file or overwrite existing
    if not (first_odd and first_even):
        # These will determine whether the first odd or even have already been identified
        if not first_odd and mode == 'odd':
            first_odd = True
        
        if not first_even and mode == 'even':
            first_even = True

        with open(f'{mode}.txt', 'w') as odd_or_even_file:
            odd_or_even_file.write(f'{str(int(pow(number, exponent)))}\n')
    else:
        with open(f'{mode}.txt', 'a') as odd_or_even_file:
            odd_or_even_file.write(f'{str(int(pow(number, exponent)))}\n')