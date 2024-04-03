'''
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15
 

Constraints:

1 <= s.length <= 105
s consists of lowercase letters.
'''
#solution
class Solution:
    def countHomogenous(self, s: str) -> int:
        new_list=[]
        str1=''
        sum_list=[]
        for i in range(0,len(s)):
            if i==0:
                str1+=s[i]
            elif s[i]==str1[-1]:
                str1=str1+s[i]
            else:
                new_list.append(str1)
                str1=''
                str1+=s[i]
        new_list.append(str1)

        
        for i in new_list:
           new_sum=len(i)*(len(i)+1)
           new_sum=int(new_sum/2)
           sum_list.append(new_sum)
        sum1=sum(sum_list)

        return sum1 % (10**9+7)

        return 13
            


        