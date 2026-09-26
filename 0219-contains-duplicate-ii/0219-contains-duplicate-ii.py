class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for current_index,num in enumerate(nums):
            if num in seen:
                if current_index-seen[num]<=k:
                    return True
            seen[num] = current_index
        return False            