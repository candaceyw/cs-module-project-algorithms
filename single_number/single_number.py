'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # array has values
    result = []
    #
    # # loop through each index item and check list for dup
    for i in arr:
        #     # if it doesn't have a pair
        #     # append to new list
        if i not in result:
            result.append(i)

        #     # if it has a pair remove
        else:
            result.remove(i)

    # # return integer
    return result[0]


# Time complexity : O(n)O(n). We only iterate through \text{nums}nums,
# so the time complexity is the number of elements in \text{nums}nums.
# Space complexity : O(1)O(1).
# no_dup = 0
# for i in arr:
#     no_dup ^= i
# return no_dup


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

    # return 2 * sum(set(arr)) - sum(arr)
    # worst solution
