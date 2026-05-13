
#brute force lrcr#

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_length = 0

        for i in range(len(s)):
            map, count = {},0
            for j in range(i,len(s)):
                map[s[j]] = map.get(s[j],0)+1

                count = max(count,map[s[j]])

                if (j-i+1)-count<=k:
                    max_length = max(max_length,j-i+1)


        return max_length


        
                



sol = Solution()

print(sol.characterReplacement("AABABBA",1))