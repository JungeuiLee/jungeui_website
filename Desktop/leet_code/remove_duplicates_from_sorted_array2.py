class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in (range(1, len(nums)-1)):
            if nums[i] == nums[j]: # 일단 i 인덱스 바로 뒤 j 인덱스 변수 확인, 만약 같다면 다음 인덱스 확인
                j += 1
                if nums[i] == nums[j]: # 만약 i 인덱스로 부터 2열 뒤에도 같다면 
                    nums[j] = nums[j + 1]
                else: # i 인덱스 2칸 뒤가 다르다면 초기 인덱스 이동
                    i += 1
                j = i + 1

            elif nums[i]!= nums[j]: # 만약 i 인덱스 바로 뒤 j의 변수가 다르다면 초기 인덱스 이동
                i += 1

        i = 1
        
        a = 2
        
        for b in range(2, len(nums)):
            if nums[b] != nums[a - 2]:
                nums[a] = nums[b]
                a += 1
        return a


test = Solution()
print(test.removeDuplicates(nums = [1,1,1,2,2,3]))
print(test.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))