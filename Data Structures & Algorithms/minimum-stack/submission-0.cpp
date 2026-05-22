class MinStack {
public:
    vector<int> st;
    vector<int> min;
    MinStack() {
    }
    
    void push(int val) {
        st.push_back(val);
        if (min.size() == 0) {
            min.push_back(val);
        } else {
            int current_min = min.back();
            min.push_back(current_min > val ? val : current_min);
        }
    }
    
    void pop() {
        st.pop_back();
        min.pop_back();
    }
    
    int top() {
        return st.back();
    }
    
    int getMin() {
        return min.back();
    }
};
