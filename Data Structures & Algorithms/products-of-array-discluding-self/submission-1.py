class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Make a list for multiplication from left to right
            #Add (or multiply) a list of multipications from right to left

        left = [0] * len(nums)
        left[0] = 1
        left[1] = nums[0]
        for i in range(2, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        print(left)
        
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            left[i] = left[i] * right
            right *= nums[i]
        
        return left



        