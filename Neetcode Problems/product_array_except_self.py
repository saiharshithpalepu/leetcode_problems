'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
#solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        postfix=1
        prefix_array=[1 for i in range(len(nums))]
        postfix_array=[1 for i in range(len(nums))]

        for i in range(len(nums)-1):
            prefix=prefix*nums[i]
            prefix_array[i+1]=prefix

        for i in range(len(nums)-1,0,-1):
            postfix=postfix*nums[i]
            postfix_array[i-1]=postfix 

        return [prefix_array[i]*postfix_array[i] for i in range(len(nums))]
        
        




       


        