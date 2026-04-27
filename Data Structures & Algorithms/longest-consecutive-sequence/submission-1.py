class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #2,3,4,5
        #10
        #20
        #Not integer less than the starting integer
        hashset = set()
        for num in nums:
            hashset.add(num)
        print(hashset)

        longest = 0
        for num in hashset:
            if num - 1 not in hashset:
                current = 1
                target = num + 1
                while target in hashset:
                    current += 1
                    target += 1
                longest = max(longest, current)
        return(longest)