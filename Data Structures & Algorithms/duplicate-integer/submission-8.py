class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        return len(nums) > len(no_duplicates)