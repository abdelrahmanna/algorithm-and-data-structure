class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        i = 0
        while i < len(nums) - 3:
            while 0 < i < len(nums) - 3 and nums[i] == nums[i-1]: i += 1
            _target = target - nums[i]
            j = i + 1
            while j < len(nums)-2:
                while i+1 < j < len(nums)-2 and nums[j] == nums[j-1]: j += 1
                _target_ = _target - nums[j]

                a, z = j+1, len(nums) - 1
                while a < z:
                    print(a, z, i, j)
                    print(_target_)
                    if (nums[a] + nums[z] == _target_):
                        output.append([nums[i], nums[j], nums[a], nums[z]])
                        print("yep")
                        while a < z and nums[a] == nums[a+1]: a += 1
                        while a < z and nums[z] == nums[z-1]: z -= 1
                    
                    print("-----------------------------------")
                    if nums[a] + nums[z] > _target_:
                        z -= 1
                    else:
                        a+=1
                j+=1
            i+=1

        return output

if __name__ == "__main__":
    
    solution = Solution()
    # [-2, -1, -1, 1, 1, 2, 2] -2 + 2 + 0 + 
    print(solution.fourSum([-2,-1,-1,1,1,2,2],0))