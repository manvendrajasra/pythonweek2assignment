n = int(input())  # number of elements in the set
s = set(map(int, input().split()))  # initialize the set with integers
m = int(input())  # number of commands

# Sort the set to ensure deterministic popping
s = sorted(s)

# Process each command
for _ in range(m):
    command = input().split()
    operation = command[0]
    
    if operation == "pop":
        # Simulate pop from a sorted set to maintain order
        if s:
            s.pop(0)
    elif operation == "remove":
        try:
            s.remove(int(command[1]))
        except ValueError:
            pass  # Ignore the error if the element is not in the set
    elif operation == "discard":
        if int(command[1]) in s:
            s.remove(int(command[1]))

# Convert list back to set and print the sum of the remaining elements
print(sum(s))
