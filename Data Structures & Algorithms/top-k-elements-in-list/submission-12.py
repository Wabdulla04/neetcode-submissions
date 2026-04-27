class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, count in count.items():
            freq[count].append(num)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans





    #Time: O(nlogk)
    #Space O(n + k)
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