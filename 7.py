def main():
    # Read the number of test cases
    n = int(input())
    
    # Process each test case
    for _ in range(n):
        try:
            # Read input values for a and b
            a, b = input().split()
            
            # Convert a and b to integers and perform integer division
            result = int(a) // int(b)
            print(result)
        
        # Handle ZeroDivisionError
        except ZeroDivisionError as e:
            print("Error Code:", e)
        
        # Handle ValueError (e.g., when the input is not a valid integer)
        except ValueError as e:
            print("Error Code:", e)

# Run the main function
if __name__ == "__main__":
    main()
