class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) {
            return 0;
        }
        int l = 0;
        int r = 1;
        int max_size = 1;
        unordered_set<char> window;
        window.insert(s[0]);
        while (r < s.size()) {
            if (window.contains(s[r])) {
                max_size = max(max_size, (int)window.size());
                while (s[l] != s[r]) {
                    window.erase(s[l]);
                    l++;
                }
                l++;                
            } else {
                window.insert(s[r]);
            }
            r++;
        }
        return max((int)window.size(), max_size);
    }
};
