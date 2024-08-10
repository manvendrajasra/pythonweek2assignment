def print_rangoli(size):
    # Creating the list of alphabets
    import string
    alphabets = string.ascii_lowercase
    
    # Initialize a list to store the rangoli lines
    lines = []
    
    # Generate the pattern
    for i in range(size):
        # Select the required letters
        s = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size])
        # Center the pattern with '-'
        lines.append(s.center(4*size-3, '-'))
    
    # Print the rangoli
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)