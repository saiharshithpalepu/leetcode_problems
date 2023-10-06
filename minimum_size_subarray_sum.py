'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

'''
solution

1.create a left pointer
2.create a variable which is total
3.create a result variable which stores the length of minimum subarray which equals to total
4.run the for loop starting from the zeroth index
5.increase the total total+=nums[i]
6.while total is greater than or eqal to the target
7.assign result = min(right-left+1,result)
8.shift the left pointer
9.decrease the total with the left pointer element
10.if result is equal to intialised value then return 0
11. otherwise return result
'''

#solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        result=float('inf')
        for right in range(0,len(nums)):
            total+=nums[right]
            while total>=target:
                total-=nums[left]
                result=min(right-left+1,result)
                left+=1
        if result==float('inf'):
            return 0
        else:
            return result