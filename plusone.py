class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int("".join(map(str, digits)))+1
        arr=[]
        for i in str(a):
            arr.append(int(i))
        return arr
        
        
