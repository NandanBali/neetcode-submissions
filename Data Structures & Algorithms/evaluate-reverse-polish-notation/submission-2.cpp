class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> n;
        for (const auto& token : tokens) {
            if (token == "+") {
                int r1 = n.back(); n.pop_back();
                int r2 = n.back(); n.pop_back();
                n.push_back(r2 + r1);
            } else if (token == "-") {
                int r1 = n.back(); n.pop_back();
                int r2 = n.back(); n.pop_back();
                n.push_back(r2 - r1);
            } else if (token == "*") {
                int r1 = n.back(); n.pop_back();
                int r2 = n.back(); n.pop_back();
                n.push_back(r2 * r1);
            } else if (token == "/") {
                int r1 = n.back(); n.pop_back();
                int r2 = n.back(); n.pop_back();
                n.push_back(r2 / r1);
            } else {
                n.push_back(stoi(token));
            }
        }
        return n.back();
    }
};