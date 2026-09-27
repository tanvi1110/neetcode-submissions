class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = sorted(nums)
        for i in range(len(nums) - 1):
            if lst[i] == lst[i + 1]:
             return True
        return False