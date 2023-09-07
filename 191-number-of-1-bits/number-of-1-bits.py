class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        if n > 0:
            while n > 0:
                if n % 2 == 1:
                    count += 1
                # print("remainder:", n % 2, "quotient:", n // 2)
                n = n // 2

        return count
        