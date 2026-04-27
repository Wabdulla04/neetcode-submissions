class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [strs]

        countS = {}
        for i in range(len(strs)):
            tempArray = [0] * 26
            for j in strs[i]:
                tempArray[ord(j) - ord('a')] += 1
            key = tuple(tempArray)
            if key not in countS:
                countS[key] = []
            countS[key].append(strs[i])
        return list(countS.values())