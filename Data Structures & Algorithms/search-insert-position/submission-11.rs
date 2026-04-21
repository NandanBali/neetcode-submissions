impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        use std::cmp::Ordering;

        let mut low: usize = 0;
        let mut high: usize = nums.len() - 1;

        if nums[high] < target {
            return high as i32 + 1;
        } else if nums[low] > target {
            return low as i32;
        }

        while low <= high {
            let mid = low + (high - low) / 2;

            if high - low <= 1 {
                if nums[low] == target {
                    return low as i32;
                } else {
                    return low as i32 + 1;
                }
            }
 
            match nums[mid].cmp(&target) {
                Ordering::Greater => {
                    high = mid;
                    if !(nums[mid - 1] < target){
                        high -= 1;
                    }
                },
                Ordering::Less => {
                    low = mid;
                    if !(nums[mid+1] > target) {
                        low += 1;
                    }
                },
                Ordering::Equal => {
                    return mid as i32;
                }
            }
       }
        low as i32 + 1
    }
}
