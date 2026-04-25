class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        if len(a)%2!=0:
            b=len(a)//2
            return a[b]
        else:
            b=len(a)//2
            c=b+1
            d=(b-1)
            e=(c-1)
            f=a[d]
            g=a[e]
            return (f+g)/2       
