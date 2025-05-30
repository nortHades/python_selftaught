# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:


# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        # get unique num
        num_unique = list(num_count.keys())
        k = 0
        for i in reversed(range(len(nums))):
            # check if the frequency > 1, remove the element and --
            if num_count[nums[i]] > 1:
                num_count[nums[i]] = num_count.get(nums[i], 0) - 1
                nums.pop(i)
                k += 1
                print(nums)
        return k

    def removeDuplicates2(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


nums = [1, 1, 2]
solution = Solution()
solution.removeDuplicates(nums)
