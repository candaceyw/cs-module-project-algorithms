'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # loop through array
    for i in arr:
        # check index for 0
        if i == 0:
            # if zero push to end
            arr.append(arr.pop(arr.index(0)))

    # return all integers
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")