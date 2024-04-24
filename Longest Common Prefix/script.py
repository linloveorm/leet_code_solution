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
            # del strs[strsLenIndex]
            print(strs)
            all_the_same = all(element == strs[0] for element in strs)
            all_same_size = all(len(element) == len(strs[0]) for element in strs)
            print(all_the_same)
            if all_the_same:
                print("Hi")
                return strs[0]
            else:            
                for i in range(1, len(shortestStr)+1):
                    print("Yes: ",shortestStr[:i])
                    
                    all_prefix = all(item[:i] == shortestStr[:i] for item in strs)
                    print("No: ",all_prefix)
                    
                    if all_prefix:
                        print("Test: ",shortestStr[:i])
                        prefix = shortestStr[:i]
                        if len(shortestStr) == 1 or i == len(shortestStr):
                            return prefix
                        
                    else:
                        print("prefix ",prefix)
                        return prefix
                

        

def main():
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    strs3 = ["ab", "a"]
    strs4 = ["flower","flower","flower","flower"]
    strs5 = ["a", "b"]
    strs6 = ["cir", "car"]
    strs7 = ["reflower","flow","flight"]
    strs8 = ["aaa", "aa", "aaa"]


    solution = Solution()
    prefix = solution.longestCommonPrefix(strs8)
    print(prefix)
    




main()














                # for item in strs:
                #     if shortestStr[:i] == strs[:i]:

            # if all_same_size:
            #     for j in range(len(shortestStr)+1):
            #         print(j)
            #         for item in strs:
            #             # print(shortestStr)
            #             # print(item)
            #             if j == 0:
            #                 if shortestStr == item:
            #                     return shortestStr
            #             else:
            #                 if shortestStr[:j] == item[:j]:
            #                     return shortestStr[:j]
            #                 else:
            #                     continue
            #             # print(shortestStr[:-j])
            #             # print(item[:j])
            #             # if shortestStr[:j] == item[:j]:
            #             #     return shortestStr[:j]
            # else:

            # for i in range(len(shortestStr)+1):
            #     previous = prefix
            #     # if i == len(shortestStr):
            #     #     print("yes")
            #     if i == 0 or len(shortestStr) == 1:
            #         prefix = shortestStr
            #     else:
            #         prefix = shortestStr[:-i]
                
            #     if len(prefix) != 0:
            #         print(prefix)
            #         if i == 0:
            #             all_prefix = all(item == prefix for item in strs)
            #             print("--", str(all_prefix))
            #         else:
            #             all_prefix = all(item[:i] == prefix for item in strs)
            #             print("++", str(all_prefix))
                    
                    # if all_same_size:
                        
                    
                    # if all_prefix:
                    #     return prefix
                    # else:
                    #     continue
                    # print(prefix)
                    # all_prefix = all(item[:i] == prefix for item in strs)
                    # for it in strs:
                    #     print(it[:i])
            
                        
                    # if all_prefix:
                    #     print(prefix)
                    #     return prefix
                    
                # previous = prefix
                # if i == 0:
                #     prefix = shortestStr
                # else:
                #     prefix = shortestStr[:i] 
                # # print(prefix)       
                # # print(previous)    
                # for item in strs:
                #     if previous != "":
                #         if item[:i] != prefix:
                #             return prefix
                    # print(item[:len(prefix)]," : ", prefix)
                    # if prefix in item[:len(prefix)]:
                        # return prefix
                #     if item[:len(prefix)] == prefix:
                # #         if len(previous) == 0:
                # #             return prefix
                # #         else:
                #         return previous
                
                # all_prefix = all(element[:len(prefix)] == strs[0][:len(prefix)] for element in strs)
                # print(strs[0][:len(prefix)])
                # if all_prefix:
                #     prefix = shortestStr[:i]
                # else:
                #     return prefix

            # print(all_same_size)
            # if not all_the_same and not all_same_size:
            #     if all_the_same:
            #         return strs[0]
            #     # elif all_same_size and not all_the_same:
            #     #     return ""
            #     else:            
            #         for i in range(len(shortestStr)):
            #             # print(len(shortestStr))
            #             previousPrefix = prefix
                        
            #             if len(shortestStr) == 1:
            #                 prefix = shortestStr
            #             else:
            #                 prefix = shortestStr[:i]
            #             # print(prefix)
            #             # if len(prefix) != 0:
            #             for item in strs:
            #                 print(item[:len(prefix)] )
            #                 # if len(shortestStr) == 1 and not all_same_size:
            #                 #     return shortestStr          
                            
            #                 if prefix not in item[:len(prefix)] and len(shortestStr) > 1:
            #                     # print(item[:len(prefix)])
            #                     return previousPrefix
            #                 elif prefix in item[:len(prefix)] and len(shortestStr) == 1:
            #                     return prefix
                            
            # else:
            #     return ""
                            

                            
                        
                        # elif all_same_size and not all_the_same:
                        #     return ""
                        
                        # elif len(prefix) == 1 and prefix in item[:len(prefix)]: