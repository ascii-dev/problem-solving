class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        output = []
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                output.append(nums[left]**2)
                left += 1
            else:
                output.append(nums[right]**2)
                right -= 1
            
        return output[::-1]
