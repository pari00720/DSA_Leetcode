class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        # Loop backwards from the second-to-last element to the first
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        # If the goalpost reaches the start, the path exists
        return goal == 0
