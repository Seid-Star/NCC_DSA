class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        a=len(mat)
        b=len(mat[0])
        arr=[]
        for i in range(a):
            for j in range(b):
                if mat[i][j]==1:
                    arr.append((i,j))
        count=0
        for i,j in arr:
            if sum(mat[i])==1 and sum(mat[x][j] for x in range(a))==1:
                count+=1
        return count

        
