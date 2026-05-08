#------------------Sliding window-----------------------------#

#-----fixed window template-----------------------------------#

# window = initial_window

# for right in range(k, len(arr)):

#     add new item

#     remove old item

#     update answer

# class Solution:

#     def test(self,nums:list[int],k:int):
#         window_sum = sum(nums[:k])
#         maxsum = window_sum

#         for i in range(k,len(nums)):
#             window_sum += nums[i]

#             window_sum-= nums[i-k]

#             maxsum = max(maxsum,window_sum)

#         return maxsum



# sol = Solution()

# print(sol.test([1,2,3,4,5],3))

#-----------------------Dynamic window----------------------------#

# left = 0

# for right in range(len(arr)):

#     # expand window

#     while condition is bad:

#         # shrink window
#         left += 1

    # calculate answer

# class Dynamic:

#     def dynamic(self,s:str):
#         left = 0
#         seen = set()

#         maxx = 0

#         for right in range(len(s)):

#             while s[right] in seen:
#                 seen.remove(s[left])
#                 left+=1
#             seen.add(s[right])
#             maxx = max(maxx, right-left+1)
#         return maxx
            



# d = Dynamic()

# print(d.dynamic("abcabcbb"))