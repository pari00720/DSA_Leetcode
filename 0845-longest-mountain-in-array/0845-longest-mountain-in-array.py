class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        max_length = 0
        base = 0
        
        while base < n - 2:
            # Step 1: Find the start of an upward slope
            if arr[base] < arr[base + 1]:
                peak = base
                
                # Walk up to the peak of the mountain
                while peak + 1 < n and arr[peak] < arr[peak + 1]:
                    peak += 1
                    
                # Step 2: Ensure there is a downward slope after the peak
                if peak + 1 < n and arr[peak] > arr[peak + 1]:
                    end = peak
                    
                    # Walk down to the base/end of the mountain
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                        
                    # Step 3: Calculate length and update max tracking
                    current_mountain_len = end - base + 1
                    max_length = max(max_length, current_mountain_len)
                    
                    # Move base to the end of this mountain to avoid re-walking
                    base = end
                else:
                    # If it went up but didn't go down, skip this peak
                    base = peak + 1
            else:
                # Flat or downhill, move to the next starting point
                base += 1
                
        return max_length
