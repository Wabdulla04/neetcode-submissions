class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(numbers):
            if num in res:
                return [res[num] + 1, i + 1]
            res[target - num] = i


    
#1, 2, 3, 4
#1 indexed, don't start at 0 

        