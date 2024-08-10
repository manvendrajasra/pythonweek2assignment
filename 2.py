def average(array):
# Convert array to a set to remove duplicates
    unique_elements = set(array)
    
    # Calculate the average
    avg = sum(unique_elements) / len(unique_elements)
    
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)