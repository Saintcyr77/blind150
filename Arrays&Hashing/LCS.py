#brute force o(n)
# class Solution:
#     def lcs(self,nums:list[int])->int:
        
#         hashset = set(nums)

#         res = 0

#         for i in range(len(sorted(nums))):

#             streak, cur = 0, nums[i]

#             while cur in hashset:
#                 cur+=1
#                 streak+=1

#             res = max(streak,res)

#         return res

#----------------------------------------onlogn not on2 since both loops run on i and i is never reset-------------------------------#


# class Solution:
#     def lcs(self,nums:list[int])->int:

#         if not nums:
#             return 0

#         nums.sort()

#         res = 0

#         streak, cur = 0, nums[0]

#         i = 0

#         while i<len(nums):

#             if cur!=nums[i]:
#                 cur = nums[i]
#                 streak = 0

#             while i<len(nums) and nums[i]==cur:
#                 i+=1
            
#             streak+=1
#             cur+=1

#             res = max(streak,res)

#         return res
                
           

class Solution:
    def lcs(self,nums:list[int])->int:
        hashset = set(nums)

        longest = 0
        counter= 0

        for num in nums:
            if num-1 not in hashset:
                counter = 1
            while num+counter in hashset:
                counter+=1
                print(counter)

            longest = max(longest,counter)

        return longest
                

      


sol = Solution()

print(sol.lcs([9,1,4,7,3,-1,0,5,8,-1,6]))