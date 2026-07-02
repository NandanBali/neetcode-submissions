class Solution {
public:
    int optimal(int x, vector<int>& cache) {
        if (cache[x] != -1) {
            return cache[x];
        }

        int res = 0;
        for (int i = x; i > 0; i--) {
            res = max(i * optimal(x-i, cache), res);
        }
        cache[x] = res;
        return res; 
    }

    int integerBreak(int n) {
        if (n > 1 && n < 4) {
            return n - 1;
        } 
        vector<int> cache(n+1, -1);
        cache[0] = 1;
        cache[1] = 1;
        return optimal(n, cache);
    }
};