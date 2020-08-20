'''
Input: an integer
Returns: an integer
'''
# can eat 1, 2, or 3 cookies
#output is number of ways that a given number of cookies can be eaten
#base cases:
    #if n == 0 return 1
    #if n < 0 return 0 
#if current cookie is equal to n return 1
# if the length of n is greater than 3 there are three options available
# if n > 0:
#eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# def eating_cookies(n):

#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
        # base case
     if n == 0:
         return 1
     elif n < 0:
         return 0
     # check if the work has already been done
     # by looking in the cache
     elif cache is not None and cache[n] > 0:
         # return the previously computed answer and don't recurse
         return cache[n]
     else:
         # might need to create our cache for the first time
         if cache is None:
             # initialize an empty list for a cache based off of testing
             cache = [0 for i in range(n + 1)]
             # store the value of the recursive call expression in out cache
         cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

     return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


