class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create a dictionary to hold the numbers : indices
        num_map = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in num_map:
                return [i, num_map[difference]]

            num_map[num] = i

        return None
        