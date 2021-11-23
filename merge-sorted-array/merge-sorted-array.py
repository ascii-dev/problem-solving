class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        counter1 = counter2 = result_counter = 0
        
        while counter1 < m and counter2 < n:
            if nums1_copy[counter1] < nums2[counter2]:
                nums1[result_counter] = nums1_copy[counter1]
                counter1 += 1
            else:
                nums1[result_counter] = nums2[counter2]
                counter2 += 1
            
            result_counter += 1
        
        if counter1 < m:
            for num in nums1_copy[counter1:]:
                nums1[result_counter] = num
                result_counter += 1
        
        if counter2 < n:
            for num in nums2[counter2:]:
                nums1[result_counter] = num
                result_counter += 1

        