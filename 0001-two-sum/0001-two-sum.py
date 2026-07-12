class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Stores seen numbers as keys and their indices as values
        seen_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement was already seen, return its index and current index
            if complement in seen_map:
                return [seen_map[complement], i]
            
            # Otherwise, cache the current number and its index
            seen_map[num] = i
            
        return []
