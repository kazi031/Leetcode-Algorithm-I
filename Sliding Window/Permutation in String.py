class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = 0
        for i in s1:
            unique_hash = ord(i)%77
            c = c + (ord(i)*unique_hash) + unique_hash
        #print(c) 

        left = 0
        ascii_count = 0
        for right in range(len(s2)):
            unique_hash = ord(s2[right])%77
            ascii_count = ascii_count + (ord(s2[right])*unique_hash) + unique_hash
            if ascii_count > c or right-left+1 > len(s1):
                unique_hash = ord(s2[left])%77
                ascii_count = ascii_count - (ord(s2[left])*unique_hash) - unique_hash
                left += 1
                if ascii_count == c and right-left+1 == len(s1):
                    return True
            elif ascii_count == c and right-left+1 == len(s1):
                return True
        return False
