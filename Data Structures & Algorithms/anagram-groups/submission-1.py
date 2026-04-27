class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for word in strs:
            letters = [0] * 26

            for letter in word:
                letters[ord(letter) - ord('a')] += 1

            grouped_anagrams[tuple(letters)].append(word)
        return list(grouped_anagrams.values())