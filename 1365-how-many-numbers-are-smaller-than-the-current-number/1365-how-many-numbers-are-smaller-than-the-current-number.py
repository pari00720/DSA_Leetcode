class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        lookup={}
        for i,num in enumerate(sorted_nums):
            if num not in lookup:
                lookup[num]=i
        return[lookup[num]for num in nums ]