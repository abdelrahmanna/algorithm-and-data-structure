def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}
        
        for i in range(0, len(nums)):
            key = target - nums[i]
            
            if (nums[i] in numsDict):
                return [i, numsDict[nums[i]]]
            numsDict[key] = i