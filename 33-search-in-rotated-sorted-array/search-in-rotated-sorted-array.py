class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1  # the index of target in nums
        left = 0
        right = len(nums) - 1
        while left <= right:
            # if we are in the sorted part of nums
            if nums[left] < nums[right]:
                # regular binary search
                mid = (left + right) // 2
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                elif nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[left]:
                    if (target >= nums[left]) and (target <= nums[mid]):
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if (target >= nums[mid]) and (target <= nums[right]):
                        left = mid + 1
                    else:
                        right = mid - 1

        return result

