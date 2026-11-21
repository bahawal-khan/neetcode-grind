class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        longest = 0
        for num in num_sets:
            if num-1 not in num_sets:
                count = 1
                while num + count in num_sets:
                    count = count +1 
                longest = max(longest,count)
        return longest