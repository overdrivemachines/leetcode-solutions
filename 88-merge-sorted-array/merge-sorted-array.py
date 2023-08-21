class Solution:
    def merge_old(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        i, j = 0, 0
        holding = list()
        while i < m and j < n:
            if len(holding) > 0 and holding[0] < nums1[i] and holding[0] < nums2[j]:
                holding.append(nums1[i])
                nums1[i] = holding.pop(0)
                i += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                holding.append(nums1[i])
                nums1[i] = nums2[j]
                i += 1
                j += 1

            # print(f"i: {i}, nums1: {nums1}, nums2: {nums2}, j: {j}, holding: {holding}")

        if i < m:
            # print("i < m, i: ", i)
            while len(holding) > 0:
                if holding[0] < nums1[i]:
                    holding.append(nums1[i])
                    nums1[i] = holding.pop(0)
                elif i >= m:
                    nums1[i] = holding.pop(0)

                # print(f"i: {i}, nums1: {nums1}, holding: {holding}")

                i += 1

        if j < n:
            print("j < n, j: ", j)
            while j < n:
                if len(holding) > 0 and holding[0] < nums2[j]:
                    nums1[i] = holding.pop(0)
                else:
                    nums1[i] = nums2[j]
                    j += 1
                i += 1

        while len(holding) > 0:
            nums1[i] = holding.pop(0)
            i += 1

        # print("final: ", nums1)
        # print(holding)

    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1