class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]==nums[j] and i<j):
                    counter = counter +1
        return counter          
                    

def main():
    nums=[1,2,3,1,1,3]
    s=Solution()
    counter=s.numIdenticalPairs(nums)
    print(counter)


if __name__ == "__main__":
    main()    