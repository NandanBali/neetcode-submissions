class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }
        
        int i = 0;
        while( i <= s2.size() - s1.size()) {
            if (s1.contains(s2[i])) {
                vector<int> cf(26,0);
                for (auto& x : s1) cf[x-'a']++;
                cout << i << endl;
                for (auto& x: s2.substr(i, s1.size())) {
                    cf[x-'a'] = max(0, cf[x-'a']-1);
                }
                int s = 0;
                for (auto& x: cf) s += x;
                if (s == 0) return true;
                i++;
            } else {
                i++;
            }
        }

        return false;
    }
};
