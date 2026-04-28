import heapq

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

sol.utilityFunc([1,1,1,2,2,3],2)