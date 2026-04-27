class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr=[]
        brr=[]
        for i in nums:
            if i%2==0:
                arr.append(i)
            else:
                brr.append(i)
        return arr+brr
