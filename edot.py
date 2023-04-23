'''
filename: edot.py

Takes in a file input, distinguishes odd from even, and then double or triple them.

1. Take a file input
2. Iterate through all the numbers from file input
    - If even, then double and append to even.txt file
    - If odd, then triple and append to odd.txt file
3. Remember to close the txt file! (Use with operator for a foolproof execution!)

'''

def edot(file_path):

    # Look for file input (integers.txt by default) file
    file_path = 'integers.txt' if file_path == '' else file_path
    try:
        with open(file_path, 'r') as numbers:
            pass

    except FileNotFoundError:
        raise f'File {file_path} does not exist.'