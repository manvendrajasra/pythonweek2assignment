def merge_the_tools(s, k):
    # Iterate over the string in steps of k
    for i in range(0, len(s), k):
        # Get the substring of length k
        substring = s[i:i+k]
        
        # Use a dictionary to maintain the order and uniqueness of characters
        seen = {}
        result = []
        
        # Iterate over each character in the substring
        for char in substring:
            # Add the character to the result if it hasn't been added before
            if char not in seen:
                seen[char] = True
                result.append(char)
        
        # Print the processed substring as a string
        print(''.join(result))
        
     
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)