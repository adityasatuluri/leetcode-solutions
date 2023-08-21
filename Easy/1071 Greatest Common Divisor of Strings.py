#1071. Greatest Common Divisor of Strings
'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

#code
#---------------------------------------------------------------------------------------------------------

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)  # Ensure str1 is longer
        
        if not str2:
            return str1
        
        if str1.startswith(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''


#---------------------------------------------------------------------------------------------------------
#explianation:

'''In this code, I've completed the gcdOfStrings method inside the Solution class. 
This method follows the same recursive logic I explained earlier. 
It first checks which string is longer and makes sure str1 is the longer one before proceeding. 
Then, it checks for cases where str2 is a prefix of str1 and shortens str1 accordingly. 
Finally, if there's no common divisor, it returns an empty string.'''