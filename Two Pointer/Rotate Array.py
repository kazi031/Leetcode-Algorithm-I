class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        dummy = 0
        n = len(nums)
        k = k % n
        c = 0
        while c < n-k:
            temp = nums.pop(dummy)
            nums.append(temp)
            c += 1