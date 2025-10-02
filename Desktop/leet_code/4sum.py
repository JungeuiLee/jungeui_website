
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        resultLst = []
        def backtrack(start, path):
            if len(path) == 4:
                result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
 
        result2 = 0
        for lst in range(len(result)):
            # print(result[lst])
            for index in range(len(result[lst])):
                result2 += result[lst][index]
            if result2 == target:
                resultLst.append(result[lst])
            result2 = 0
        # return resultLst
        uniqueSet = []
        for i in resultLst:
            if i not in uniqueSet:
                uniqueSet.append(i)
        return uniqueSet
    
test = Solution()
print(test.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(test.fourSum(nums = [-493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,-180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,481,492], target = 6189))
