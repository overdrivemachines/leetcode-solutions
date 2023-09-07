class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count

    def countBits(self, n: int) -> List[int]:
        li = list()
        i = 0
        count = 0

        while i <= n:
            # find the number of 1s in the binary representation of i
            li.append(self.hammingWeight(i))
            i += 1

        return li