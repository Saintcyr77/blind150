# complexity o(m) where m is length of the string we are encoding and decoding. We are using a delimiter to separate the sizes of the strings and the strings themselves. We first encode the sizes of the strings followed by a delimiter and then the strings themselves. During decoding, we first read the sizes of the strings until we reach the delimiter and then we read the strings based on their sizes.

# class Solution:

#     def encode(self, strs:list[str])-> str:
#         if len(strs)==0:
#             return ""
        
#         size = []
#         res = ""

#         for i in range(len(strs)):
#             size.append(len(strs[i]))

#         for sz in size:
#             res+=str(sz) 
#             res+=','

#         res+='#'

#         for strr in strs:
#             res+=strr

#         print(res)

#         return res


    

#     def decode(self,s:str)->list[str]:

#         if not s:
#             return []
        
#         sizes,res,i = [],[],0 

#         while s[i]!='#':
#             cur = ""

#             while(s[i]!=','):
#                 cur+=s[i]
#                 i=i+1
#             sizes.append(int(cur))

#             i=i+1

#         i = i+1

#         for sz in sizes:
#             res.append(s[i:i + sz])
#             print(s[i:i + sz])
#             i += sz
#         return res

       
        






# sol = Solution()

# s = sol.encode(["Hello","World"])

# print(sol.decode(s))