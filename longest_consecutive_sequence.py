'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
'''
solution
1.initialize count and max variables
2. convert the given list into set and sort it
3.run the loop
4. if i is 0 then increase count to 1
5. if the difference between the current number and previous number is 1 
then increase the count
6. if it is not assign 1 to count
7.at the ending of the loop check whether count is greater than max if it is the assign to max
8. return max

'''
#solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers=sorted(list(set(nums)))
        count1=0
        max1=0
        for i in range(0,len(numbers)):
            if i==0:
                count1+=1
            else:
                if(numbers[i]-numbers[i-1]==1):
                    count1+=1
                else:
                    count1=1
            if count1>max1:
                max1=count1
        return max1