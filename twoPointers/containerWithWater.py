#---------------------------------o(n) two pointers-----------------------------#

class Solution:
    def maxArea(self, heights: list[int]) -> int:

        hei = 0

        i = 0
        j = len(heights)-1

        while i<j:

            if heights[i]<heights[j]:
                hei = max(hei,(j-i)*min(heights[i],heights[j]))
                i+=1
            else:
                hei = max(hei,(j-i)*min(heights[i],heights[j]))
                j-=1

        return hei


sol = Solution()

print(sol.maxArea([1,7,2,5,4,7,3,6]))