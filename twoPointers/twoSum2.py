
#---------------------------brute force on2----------------------------------------#
# class Solution:
#     def twoSum(self,numbers:list[int],target)->list[int]:
#         for i in range(len(numbers)-1):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i]+numbers[j]==target:
#                     return [i+1,j+1]

#---------------------------------on optimal---------------------------------------#

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        i = 0
        j = len(nums)-1

        while(i<j):
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1

                


        
        


sol = Solution()

print(sol.twoSum([2,7,11,15],9))