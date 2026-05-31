class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> x;

        for (int i = 0; i < nums.size(); i++) {

            if (x.size() > k) {
                x.erase(nums[i-k-1]);
            }
            if (x.contains(nums[i])) {
                return true;
            }
            x.insert(nums[i]);

        }
        
        return false;
    
    }

};