class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        for current in range(len(nums)):
            if nums[unique] != nums[current]:
                nums[unique + 1] = nums[current]
                unique += 1
        
        return unique + 1
        