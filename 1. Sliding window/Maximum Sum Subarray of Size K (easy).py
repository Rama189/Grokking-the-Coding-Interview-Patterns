
'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''
#mycode
def maxSubarray(nums, k):
    l = len(nums)
    z = k
    sum = 0
    max = 0
    for ind, x in enumerate(nums[:l - k + 2]):
        if z == 0:
            z = -1

        if z > 0 :
            sum = sum + x
            z = z - 1

        if z == -1:
            sum = sum + x - nums[ind - k]
        
        if sum > max:
            max = sum
    print("{}".format(max))


#answer
def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  window_start = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
  return max_sum


def main():
    # nums = [2, 3, 4, 1, 5]
    nums = [2, 1]
    k = 1
    maxSubarray(nums, k)
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N).
Space Complexity 
The algorithm runs in constant space O(1).
'''
