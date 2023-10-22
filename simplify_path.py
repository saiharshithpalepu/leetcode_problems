'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
'''

'''
solution

1.create a stack and and an empty string current
2.iterate through the path with variable i
3.if i is equal to '/' then we will have three conditions
4.if current is equal to double period then we have to pop the item from the stack 
5. we are doing this becuase .. index index we have to come out of the current directory
6.if the current is not equal to empty string and single period then we will add that string to stack
7.else in the final condition we will make the current to empty string again
8.if i is not equal to '/' then we will add i to the current
9.finally we well return the canonical path using join method and sending stack as an argument

'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        current=''
        for i in path+'/':
            if i=='/':
                if current=='..':
                    if stack:
                        stack.pop()
                elif current!='' and current !='.':
                    stack.append(current)
                current=''
            else:
                current+=i
        return '/'+'/'.join(stack)
       