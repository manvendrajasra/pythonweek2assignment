from collections import Counter

def compute_earnings():
    # Read input values
    number_of_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    
    # Count the occurrences of each shoe size
    inventory = Counter(shoe_sizes)
    
    # Number of customers
    number_of_customers = int(input())
    
    # Initialize earnings to 0
    earnings = 0
    
    # Process each customer's purchase
    for _ in range(number_of_customers):
        size, price = map(int, input().split())
        
        # If the desired size is available, process the sale
        if inventory[size] > 0:
            earnings += price
            inventory[size] -= 1  # Decrease the count of the sold shoe size
    
    # Print the total earnings
    print(earnings)

# Call the function to execute the logic
compute_earnings()
