
class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to calculate the sum of squared digits
        def get_next(num: int) -> int:
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        
        # Move pointers at different speeds until they meet or fast hits 1
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
            
        return fast_runner == 1
        