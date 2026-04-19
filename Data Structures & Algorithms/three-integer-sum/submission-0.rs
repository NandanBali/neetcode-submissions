impl Solution {
    pub fn three_sum(numbers: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = numbers.clone();
        nums.sort_unstable();
        let mut result: Vec<Vec<i32>> = vec![];
        let n = nums.len();

        if n < 3 { return result; }  // guard against underflow

        for i in 0..n - 2 {
            // skip duplicate i values
            if i > 0 && nums[i] == nums[i - 1] { continue; }
            // early exit: smallest possible sum is too big
            if nums[i] + nums[i + 1] + nums[i + 2] > 0 { break; }
            // early exit: largest possible sum is too small
            if nums[i] + nums[n - 2] + nums[n - 1] < 0 { continue; }

            let mut j = i + 1;
            let mut k = n - 1;

            while k > j {
                let sum = nums[i] + nums[j] + nums[k];
                match sum.cmp(&0) {
                    std::cmp::Ordering::Equal => {
                        result.push(vec![nums[i], nums[j], nums[k]]);
                        // advance j past duplicates
                        while j < k && nums[j] == nums[j + 1] { j += 1; }
                        // retreat k past duplicates
                        while j < k && nums[k] == nums[k - 1] { k -= 1; }
                        j += 1;
                        k -= 1;
                    },
                    std::cmp::Ordering::Greater => k -= 1,
                    std::cmp::Ordering::Less    => j += 1,
                }
            }
        }

        result
    }
}