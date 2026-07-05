class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list =[]
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                new_list.append(nums.pop(i+1))
            else:
                i=i+1
        k=len(nums)
        
        print(nums)        