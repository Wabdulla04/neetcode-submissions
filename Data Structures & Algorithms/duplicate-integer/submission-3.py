class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = []
        for i in range(len(nums)):
            if nums[i] not in cache:
                cache.append(nums[i])
            if len(cache) != len(nums[0:i+1]):
                return True
        return False

        