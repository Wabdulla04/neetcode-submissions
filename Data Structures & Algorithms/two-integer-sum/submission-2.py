class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(nums):
            if num in hashMap:
                return [hashMap[num], index]
            else:
                hashMap[target - num] = index
        