'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    output_arr = []

    for i in range(len(nums) - k +1):
        current_window = nums[i:i+k]
        current_max = max(current_window)
        output_arr.append(current_max)
    return output_arr


    # output = []
    # dq = []
    #
    # # length of dq <= k
    # # values store are indexes
    # # max contained dq[0]
    # for i, num in enumerate(nums):
    #     if dq and dq[0] < i - k + 1:
    #         dq.pop(0)
    #
    #     # while dq exists
    #     while dq and nums[dq[-1]] < num:
    #         dq.pop()
    #
    #     dq.append(i)
    #
    #     if i >= k -1:
    #         output.append(nums[dq[0]])
    #
    # return output

def sliding_windo_max_queue(nums, k):
    # create a queue that stores "useful numbers"
    # insert the first K elements
        # for each element we add
        # all smaller numbers in the queue, remove them

        # add the number to the end of the queue

    # Process the remaining elements in nums
    # from K to n-1
        # the elements at the front of the queue
        # is the largest number of the current window
        # so save that number into our output



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
