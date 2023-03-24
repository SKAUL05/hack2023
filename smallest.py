# Given an array Arr[] of N integers.
# Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
from utilities import timer


# Find the contiguous sub-array with the maximum sum and return its sum
@timer
def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]
    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


# main function to test the code
if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArraySum(arr, len(arr)))
