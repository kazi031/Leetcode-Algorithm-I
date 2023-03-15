class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split(" ")
        n = len(strings)
        c = 0
        result = ""
        for s1 in strings:
            s2 = ""
            for i in s1:
                s2 = i + s2
            if c < n-1:
                result = result + s2 + " "
            else:
                result = result + s2
            c += 1
        return result