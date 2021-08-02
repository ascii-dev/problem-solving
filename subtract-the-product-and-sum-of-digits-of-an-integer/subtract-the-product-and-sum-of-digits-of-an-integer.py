class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        while n > 0:
            current_digit = n % 10
            sum += current_digit
            product *= current_digit
            n //= 10
        
        return product - sum
