'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
solution
1.initialize left,total, result variables
2.iterate the loop making it as right variable
3.if the right is in loop the add it to total and increase count
4. if it is not in total 
5. go to else condition
6. run the while loop until left character is equal to the right character
7.increase the left character index in the loop
8. increase the left character index outside the loop
9.make total as substring [left:right+1]
10.make count as length of total string
11. if count is grater than result assign count to result
12.finally return the result

'''
#solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        total=''
        count1=0
        result=0
        for right in range(0,len(s)):
            if s[right] not in total:
                total+=s[right]
                count1+=1
            else:
                while (s[left]!=s[right]):
                    left+=1
                left+=1
                total=s[left:right+1]
                count1=len(total)
            if count1>result:
                result=count1

        return result