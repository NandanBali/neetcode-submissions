impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let k = (k as usize) % nums.len();
        if k == 0 {
            return;
        }

       nums.reverse();
       nums[..k].reverse();
       nums[k..].reverse(); 
    }
}
