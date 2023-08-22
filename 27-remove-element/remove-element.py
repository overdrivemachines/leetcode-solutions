class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        # print("nums:", nums, "val:", val)

        if len(nums) == 0:
            return 0

        i = 0
        j = len(nums) - 1

        while i <= j:
            # print("i:", i, "j:", j)
            if nums[j] == val:
                nums[j] = None
                j -= 1
            else:
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]
                    # nums[j] = None
                    j -= 1

                i += 1
                count += 1

        # print("i:", i, "j:", j)
        if i == 0 and j == 0 and nums[0] == val:
            nums[0] = None
            # return 0
        # print("nums: ", nums)

        return count