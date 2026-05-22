class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<pair<int,int>> st;
        vector<int> res;

        for (int i = 0; i < temperatures.size(); i++) {
            int t = temperatures[i];
            res.push_back(0);
            while (true) {
                if (st.size() == 0) {
                    st.push_back(make_pair(t, i));
                    break;
                }
                if (st.back().first < t) {
                    int idx = st.back().second;
                    res[idx] = i - idx;
                    st.pop_back();
                } else {
                    st.push_back(make_pair(t, i));
                    break;
                }
            }
        } 
        return res; 
    }
};
