'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#window is going to be a range == value of k
#with each move the window makes the highest value will be recorded
#the highest values will be returned to a new list
def sliding_window_max(nums, k):
    #create an array to store the max values
    #iterate through the range of values determined by k
    #find the highest value in the range 
    #shift the range
    max_values = []

    start = 0
    end = k 

    while end <= len(nums):
        max_values.append(max(nums[start:end]))
        start += 1
        end += 1
    
    return max_values





if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
