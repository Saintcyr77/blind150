import heapq

class Solution:


    def prefix(self,nums:list[int],i:int)->int:
            prod = 1
            for k in range(len(nums)):
                if k!=i:
                    prod*=nums[k]

            return prod
    
    def utilityFunc(self,nums:list[int])->list[int]:

        ans = []
        
        for i in range(len(nums)):
            if i>0:
                ans.append(self.prefix(nums,i))

            if i==0:
                prod = 1
                for i in range(len(nums)):
                    if i!=0:
                        prod*=nums[i]
                ans.append(prod)

       
        
        return ans

                        
                

    
       









sol = Solution()

print(sol.utilityFunc([1,2,4,6]))