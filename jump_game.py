'''
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
 length is 0, which makes it impossible to reach the last index.
'''

'''
solution
1.initialize reachable index to value 0
2.then iterate the loop till the len(nums)
3.if index + nums[index] is greater than or equal to reachable index
4. then we assign the value to reachable index
5.if the current index is equal to reachable index then break the loop
6. check if reachable index is greate than or equal to nums last index
7. then return the result
'''

#solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex=0
        for i in range(0,len(nums)):
            if i+nums[i]>=reachableIndex:
                reachableIndex=i+nums[i]
            if i==reachableIndex:
                break

        return reachableIndex>=len(nums)-1