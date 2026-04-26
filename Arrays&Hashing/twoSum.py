
# brute force two hashmaps
# class Solution:

#     def twoSum(self, nums:list[int], target:int)->list[int]:
        
#         h1 = {} 
#         h2 = {}

#         for i in range(len(nums)): # 1 loop o(n)
#             h1[i] = nums[i]
#             h2[i] = nums[i]

#         for key1,val1 in h1.items(): #two loops o(n2)
#             for key2, val2 in h2.items():
#                 if((key1!=key2) and (val1+val2)==target):
#                      return [key1,key2]
            
#totalcomplexity 2o(n2) we can remove constant o(n2)

#-------------------------------------------------------------------------------------------------#   
            
# optimized o(n)
# class Solution:

#     def twoSum(self, nums: list[int], target:int)->list[int]:

#         counter = target 
#         h1 = {}

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in h1:
#                 return [h1[diff],i]
#             h1[n] = i 

      




           

       



sol = Solution()

print(sol.twoSum([3,4,5,6],7))
