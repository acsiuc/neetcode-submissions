class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        if len(nums) > len(no_duplicates):
            return True
        else:
            return False