class Solution:
    def lcs(self,nums:list[int])->int:
        
        ans = []

        count = 0
        for i in range(len(nums)-1):
            ans.append(count)
            count = 0
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]+1:
                    count+=1

        sorted(ans,reverse=True)

        print(ans)


      


sol = Solution()

sol.lcs([2,20,4,10,3,4,5])