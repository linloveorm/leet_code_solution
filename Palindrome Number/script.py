class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        isOdd = True
        if len(str(x)) == 1:
            return True
        elif len(str(x)) %2 == 0:
            isOdd = True
        else:
            isOdd = False

        
        isPalidromeNo = True
        if isOdd:
            numberLen = int(len(number)/2.0)
        else:
            numberLen = int(len(number)-1/2.0)
        for i in range(numberLen):
            if number[i] != number[-(i+1)]:
                
                return not isPalidromeNo
            else:
                if i == numberLen-1 and isPalidromeNo:
                    return isPalidromeNo
                else:
                    continue

            

solution = Solution()
result = solution.isPalindrome(0)
print(result)