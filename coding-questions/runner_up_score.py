# Find the second highest (runner-up) value in a list of integers provided by the user.
# Constraints: -100 <= arr[num] <= 100

def find_runner_up():
    # reads a single line of input from the user, splits it into individual string elements, 
    # converts each string element to an integer, and then maps these into an iterable (a map object)
    arr = map(int, input().split())

    # Initialize to negative infinity. 
    # This ensures that any number in the array will be greater than these initial values.
    max_score = float('-inf')
    runner_up = float('-inf')

    for num in arr:
        if num > max_score:
            runner_up = max_score
            max_score = num
        
        # Check if num is between max_score and runner_up
        # If num is less than max_score but greater than runner_up, we have found a new second highest number.
        elif max_score > num > runner_up:
            runner_up = num
            
    print(runner_up)
