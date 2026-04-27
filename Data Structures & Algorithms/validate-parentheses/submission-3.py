class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for l in s:
            if l in hashMap:
                if stack and stack[-1] == hashMap[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return True if not stack else False