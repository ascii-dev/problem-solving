class Solution:
    def shift(self, arr: List[int], index: int) -> None:
        for i in range(len(arr) - 2, index - 1, -1):
            arr[i + 1] = arr[i]
        
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        while index < len(arr):
            if arr[index] == 0 and (index + 1) < len(arr):
                self.shift(arr, index + 1)
                arr[index + 1] = 0
                index += 2
                continue
            index += 1
        