
#brute force o(n * klogk)
from collections import defaultdict
class Solution:
    parentList = []
    def groupAnagrams(self, strs: list[str])->list[list[str]]:

        res = defaultdict(list)

        for s in strs: #o(n)

            sortedS = ''.join(sorted(s)) # sortig has time complexity o(n log n) lets call it k here
            res[sortedS].append(s)

        return list(res.values())  
    

    


sol = Solution()

print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))