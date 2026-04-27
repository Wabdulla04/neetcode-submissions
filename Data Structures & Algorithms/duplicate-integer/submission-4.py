class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set(nums)
        if len(cache) < len(nums):
            return True
        else:
             return False

        