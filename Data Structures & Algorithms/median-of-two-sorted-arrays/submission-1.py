class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        total = len(a) + len(b)
        half = total // 2
        l, r = 0, len(a) - 1

        INF = float('inf')
        while True:
            amid = (l + r) // 2
            bmid = half - amid - 2
            ar = a[amid + 1] if 0<= amid + 1 < len(a) else INF
            al = a[amid ] if 0<= amid < len(a) else -INF
            br = b[bmid + 1] if 0<= bmid + 1 < len(b) else INF
            bl = b[bmid ] if 0<= bmid < len(b) else -INF

            if al <= br and bl <= ar:
                if total % 2 == 0:
                    return (min(br, ar) + max(al, bl)) / 2
                else:
                    return min(ar, br)
            else:
                if al > br:
                    r = amid - 1
                else:
                    l = amid + 1
        return 0.0
 
        