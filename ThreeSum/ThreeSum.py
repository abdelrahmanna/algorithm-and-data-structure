def threeSum(nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()
        output = []
        for i in range(0, len(nums) - 2):
            if (i != 0 and nums[i] == nums[i-1]):
                continue
            target = 0 - nums[i]
            _sum = None
            k, j = i+1, len(nums) - 1
            while k < j:
                _sum = nums[k] + nums[j]
                if (_sum == target):
                    output.append([nums[i], nums[k], nums[j]])
                    while(k != j and nums[k] == nums[k+1]): k+=1
                    print(k,j,i)
                    while(k != j and nums[j] == nums[j-1]): j-=1
                if (_sum > target):
                    j -= 1
                else:
                    k += 1
            {}.get  
        return output


if __name__ == "__main__":
    print(threeSum([-1,0,1]))
    print(threeSum([0,1,1]))
    print(threeSum([0,0,0]))
    print(threeSum([-1,0,1,2,-1,-4]))
    print(threeSum([0,0,0,0]))