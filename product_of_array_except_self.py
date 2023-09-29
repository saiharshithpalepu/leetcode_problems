'''
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
'''
solution
1.create 5 variables prefix,postfix, finalarray, prefix array,postfix array
2.iterate the nums array if the index is 0 then store prefix as prefix multiplied by that element
3.otherwise prefix will be prefix multiplied by before element
4.append the prefixes to the array
5.similarly iterate the loop in reverse direction
6.if index== len(nums)-1 then postfix will be 1
7.otherwise postfix will be multiplied by the next element of the index in the array
8.iterate the loop in the length of nums and product of prefix and postfix to the final array
9.return the final array


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix=1
        prefix=1
        postfix_array=[]
        prefix_array=[]
        final_array=[]
        for i in range(0,len(nums)):
            if i==0:
                prefix=prefix*1
            else:
                prefix=prefix*nums[i-1]
            prefix_array.append(prefix)

        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                postfix=postfix*1
            else:
                postfix=postfix*nums[j+1]
            postfix_array.append(postfix)
        postfix_array.reverse()

        for k in range(0,len(nums)):
            final_array.append(prefix_array[k]*postfix_array[k])
        return final_array