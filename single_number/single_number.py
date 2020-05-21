'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # a = 0
    # for x in arr:
    #     a ^= x
    # return a    
    
    counts = {}
    for n in arr:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    for n, i in counts.items():        
        if i ==1:
            return n        


    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")