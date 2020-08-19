'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    result = []

    for i in arr:
        if i not in result:
            result.append(i)
        else:
            result.remove(i)
    return result[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")




    #array will not be empty
    #iterate through array to check for duplicates
    #if interger does not have duplicate return the integer

