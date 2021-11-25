class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  # O(N) + O(N) = O(N)
        occurrence = len([item for item in nums if item == val])  # O(N)
        pointer1, pointer2 = 0, len(nums) - 1
        
        while pointer1 <= pointer2:  # O(N)
            if nums[pointer1] == val:
                if nums[pointer2] == val:
                    pointer2 -= 1
                    continue
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
            pointer1 += 1
        
        return len(nums) - occurrence
        