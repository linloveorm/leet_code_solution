class Solution(object):
    def longestCommonPrefix(self, strs):
        if "" in strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix = ""
            strsLen =[len(i) for i in strs]
            strsLenIndex = strsLen.index(min(strsLen))
            shortestStr = strs[strsLenIndex]
            if min(strsLen) == 1:
                return strs[strsLenIndex]
            else:            
                for i in range(len(shortestStr)):
                    previousPrefix = prefix
                    prefix = shortestStr[:i]
                    for item in strs:
                        if prefix not in item:
                            return previousPrefix
        

def main():
    strs1 = ["reflower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    strs3 = ["ab", "a"]

    solution = Solution()
    prefix = solution.longestCommonPrefix(strs1)
    print(prefix)




main()