'''
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters 
exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

#solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}

        for i in s:
            dict1[i]=dict1.get(i,0)+1

        for j in t:
            dict2[j]=dict2.get(j,0)+1

        return dict1==dict2

           
        