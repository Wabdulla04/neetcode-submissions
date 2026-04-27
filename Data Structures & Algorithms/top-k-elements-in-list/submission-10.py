class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer



    #Time: O(nlogn)
    #Space O(n)
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        answer = []
        for i in range(k):
            answer.append(max(count, key=count.get))
            count.pop(max(count, key=count.get))
        return answer