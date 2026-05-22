class StockSpanner {
public:
    vector<pair<int, int>> st;
    StockSpanner() = default;
    
    int next(int price) {
        int sp = 1;
        while (true) {
            if (st.size() == 0) {
                st.push_back(make_pair(price, sp));
                return sp;
            }
            if (price >= st.back().first) {
                sp += st.back().second;
                st.pop_back();
            } else {
                break;
            }
        }
        st.push_back(make_pair(price, sp));
        return sp;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */