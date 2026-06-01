class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        
        int ws = 0;
        int ms = INT_MAX;
        bool d = false; 
        for (int r = 0; r < nums.size(); r++) {
            ws += nums[r];
            while (ws >= target) {
                if(!d) d = true;
                ms = min(ms, r-l+1);
                ws -= nums[l++];
            }
        }

        return d ? ms : 0;
    }
};