class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> c_f(26,0);
        int l = 0;
        int max_sz = 0;
        for (int r = 0; r < s.size(); r++) {
            c_f[s[r]-'A']++;
            while (l <= r) {
                int mcf = *max_element(c_f.begin(), c_f.end());
                if (r - l + 1 - mcf <= k) {
                    break;
                }
                c_f[s[l]-'A']--;
                l++;
            }

            max_sz = max(max_sz, r - l + 1);
        }
        return max_sz;
    }
};
