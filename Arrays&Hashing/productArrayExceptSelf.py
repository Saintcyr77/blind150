import math
# brute force on2

# class Solution:


#     def prefix(self,nums:list[int],i:int)->int:
#             prod = 1
#             for k in range(len(nums)):
#                 if k!=i:
#                     prod*=nums[k]

#             return prod
    
#     def utilityFunc(self,nums:list[int])->list[int]:

#         ans = []
        
#         for i in range(len(nums)):
#             if i>0:
#                 ans.append(self.prefix(nums,i))

#             if i==0:
#                 prod = 1
#                 for i in range(len(nums)):
#                     if i!=0:
#                         prod*=nums[i]
#                 ans.append(prod)

       
        
#         return ans

#----------------------------------optimal on---------------------------------------------------#

# class Solution:
    
#     def utilityFunc(self,nums:list[int])->int:

#         ans = []

#         zeros = nums.count(0)

#         prod = math.prod([x for x in nums if x!=0])

#         print(zeros)

#         for i in range(len(nums)):

#             if zeros>1:
#                 ans.append(0)

#             elif zeros==1:
#                 if nums[i]==0:
#                     ans.append(prod)
#                 else:
#                     ans.append(0)
#             else:
#                 ans.append(prod//nums[i])

#         return ans

       



sol = Solution()

print(sol.utilityFunc([1,2,4,6]))