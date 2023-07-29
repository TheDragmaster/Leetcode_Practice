class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A pointer
            j = half - i - 2 # B pointer

            Aleft = A[i] if i >= 0 else float("-infinity")      #Basically if anything goes out of bounds we assign it -infinity or infinity respectively 
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) <len(B) else float("infinity")

            #Will pass if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #And this is for if there is an odd amount of values in the array 
                if total % 2:
                    return min(Aright, Bright)
                # even amount of values in the array
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
            elif Aleft > Bright: 
                r = i -1
            else:
                l = i + 1