#------------------------------on2----------------------------------------#

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        res = set()
        newnum = sorted(nums)

        for i in range(len(newnum)-2):
            j = i+1
            k = len(newnum)-1

            while(j<k):
                if newnum[i]+newnum[j]+newnum[k]==0:
                    res.add((newnum[i], newnum[j], newnum[k]))
                    k-=1
                    j+=1
                elif newnum[i]+newnum[j]+newnum[k]<0:
                    j+=1
                else:
                    k-=1

        return list(res)
    


sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))