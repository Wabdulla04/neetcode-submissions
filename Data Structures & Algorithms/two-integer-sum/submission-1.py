class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in pairs:
                return [pairs[difference], i]
            else:
                pairs[num] = i
        