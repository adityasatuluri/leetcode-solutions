#75. Sort Colors
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2
'''

#code(python 3):
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''nums.sort()
        return nums'''
        left,i,right=0,0,len(nums)-1
        while(i<=right):
            if(nums[i]==0):
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
                i+=1
            elif(nums[i]==2):
                nums[right],nums[i]=nums[i],nums[right]
                right-=1
            else:
                i+=1

#one line solution:
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
'''