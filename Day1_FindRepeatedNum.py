# 找出数组中重复的数字: 0~n-1的范围内，
# 哈希表/ Set

class Solution1:
    def findRepeatNumber(self, nums:[int])->int:
        dic = set()
        for num in nums:
            if num in dic:return num
            dic.add(num)
        return -1

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1




