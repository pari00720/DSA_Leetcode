class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 1. Your sorting step (Keep it ascending)
        c = sorted(citations)
        n = len(c)
        
        # 2. Your pointers
        l = 0
        r = n - 1
        
        # 3. Add the missing binary search loop
        while l <= r:
            mid = (l + r) // 2
            
            # If citations at mid can support the remaining (n - mid) papers
            if c[mid] >= n - mid:
                r = mid - 1  # Try to find a larger H-index by moving left
            else:
                l = mid + 1  # Need higher citation counts, move right
                
        # The total number of valid papers will be left at n - l
        return n - l
