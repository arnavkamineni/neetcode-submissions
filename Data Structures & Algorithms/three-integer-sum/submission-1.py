class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outs = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            j = i+1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    outs.append([nums[i], nums[j], nums[k]])

                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    if nums[j] + nums[k] > target:
                        k -= 1
        return outs
        
            

        