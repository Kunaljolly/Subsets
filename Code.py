
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        t = []
        n = len(nums)
        for x in range(2**n):
            s = bin(x)[2:].zfill(n)  # Binary representation of x, padded with zeros
            l = []
            for i in range(n):
                if s[i] == '1':  # If the binary digit is 1, include nums[i]
                    l.append(nums[i])
            t.append(l)
        return t
