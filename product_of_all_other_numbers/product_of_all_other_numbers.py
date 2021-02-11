'''
Input: a List of integers
Returns: a List of integers
'''

#the return value is the product of all items in array except the index value
#check that array is longer than 1
#multiply each value by all other values
#divide the result by value of the index
# def product_of_all_other_numbers(arr):
    
#     if len(arr) < 1:
#         return -1

#     p = 1 #this is a starting point

#     for n in arr:
#         p *= n

#     return [p // n for n in arr]
import math
def product_of_all_other_numbers(arr):
    index = 0
    result_arr = []
    while_arr = []
    while index <= len(arr) - 1:
        while_arr = arr
        i = while_arr[index]
        while_arr.remove(while_arr[index])
        product = math.prod(while_arr)
        while_arr.insert(index, i)
        result_arr.append(product)
        index += 1
    return result_arr






if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# [2*3*4*5, 1*3*4*5, 1*2*4*5, 1*2*3*5, 1*2*3*4]