import re

def is_valid_regex(regex):
    try:
        # Try to compile the regex
        re.compile(regex)
        return True
    except re.error:
        return False

if __name__ == "__main__":
    # Read the number of test cases
    n = int(input())
    
    # Process each test case
    for _ in range(n):
        # Read the regex pattern
        pattern = input().strip()
        
        # Check if it's a valid regex and print the result
        print(is_valid_regex(pattern))
