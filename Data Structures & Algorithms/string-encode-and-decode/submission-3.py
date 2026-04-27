class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for word in strs:
            encoding += f"{len(word)}#{word}"
        return encoding

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res