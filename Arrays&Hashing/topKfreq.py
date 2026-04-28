# brute force o n* mlogm (since we sort map and keys are unique so mlogm and not nlogn)

from collections import defaultdict
from collections import deque
import heapq
# class Solution:
#     def topKfrequent(self,nums:list[int],k:int)->list[int]:
#         map = {}
#         ds = []

#         for i in range(len(nums)): #on
#             map[nums[i]] = map.get(nums[i],0)+1

#         dq = deque(sorted(map,key= lambda x:map[x],reverse=True)) #omlogm

#         print(dq)

#         for i in range(k):
#             ds.append(dq.popleft())

#         return ds 
    
#----------------------------------slightly better on*mlogk----------------------------------------------#
# 
# 
#  
    
class Solution:
    def utilityFunc(self,nums:list[int],k:int)->list[int]:

        map = {}

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0)+1

        print(map)

        heap = []

        for key, values in map.items():
            heapq.heappush(heap,(values,key))

            if len(heap)>k:
                heapq.heappop(heap)

        res  = []

        for num in heap:
            res.append(heapq.heappop(heap)[1])

        return res






sol = Solution()

print(sol.topKfrequent([1,2,2,3,3,3], 2))

