class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int pivot = 0;

        // find pivot
        while (low < high) {
            int mid = low +((high - low ) / 2);
            if (nums[mid] > nums[mid+1]) {
                pivot = mid;
                break;
            } else {
                if (nums[mid] <= nums[high]) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            }
        }

        cout << "pivot: " << pivot << '\n';
        if (target == nums[pivot])
            return pivot;
        
        if (target <= nums[nums.size() - 1]) {
            low = pivot + 1;
            high = nums.size() - 1; 
        } else {
            low = 0;
            high = pivot;
        }

        while (low <= high) {
            int mid = low + ((high-low)/2);

            if (nums[mid] > target) {
                high = mid-1;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                return mid;
            }
        }

        return -1;
   }
};
