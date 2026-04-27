class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        answer = []
        for i in range(k):
            answer.append(max(count, key=count.get))
            count.pop(max(count, key=count.get))
        return answer