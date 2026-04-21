class Solution {
public:
    int mySqrt(int x) {
        int l = 0;
        int h;
        if (x > 5) {
            h = x / 2;
        } else {
            h = x;
        }
        while (l <= h) {
            long long m = l + (h-l)/2;
            long long product = m * m;
            if (product > x) {
                h = m - 1;
            } else if (product == x) {
                return m;
            } else {
                l = m + 1;
            }
        }

        return l - 1;
    }
};