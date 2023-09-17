'''
Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''
#solution
'''
1.count the number of vowels in the substring from [0:k]
2.return the sum to the max1
3.iterate the string from k to its length
4.if kth letter is vowel add +1 to sum
5.if j-kth letter is vowel decrease the sum
6. then check if sum is greater than max
7.if it is more then assign sum to max
8. finally return max
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max1=0
        for i in range(0,k):
            if s[i] in 'aeiou':
                max1+=1
        sum1=max1
        for j in range(k,len(s)):
            if s[j] in 'aeiou':
                sum1+=1
            if s[j-k] in 'aeiou':
                sum1-=1

            if(sum1>max1):
                max1=sum1
        return max1