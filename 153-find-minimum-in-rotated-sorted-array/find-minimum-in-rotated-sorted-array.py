class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        mid = right // 2
        result = nums[mid]

        while left <= right:
            # if the list is already sorted and there is no rotation
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            mid = (left + right) // 2
            result = min(result, nums[mid])
            # we are on the left sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # we are on the right sorted portion
                right = mid - 1

        return result