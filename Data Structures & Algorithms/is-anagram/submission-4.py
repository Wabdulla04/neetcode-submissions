class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def createHash(word):
            hashWord = {}
            for letter in word:
                if letter not in hashWord:
                    hashWord[letter] = 1
                else:
                    hashWord[letter] += 1
            return hashWord
        hashS = createHash(s)
        hashT = createHash(t)
        return(hashS == hashT)