impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        use std::cmp::Ordering;
        let mut i1: usize = 0;
        let mut i2: usize = numbers.len() - 1;

        while i2 > i1 {
            let sum = numbers[i1] + numbers[i2];
            match sum.cmp(&target) {
                Ordering::Less => { i1 += 1; },
                Ordering::Greater => { i2 -= 1; },
                Ordering::Equal => { return vec![i1 as i32 + 1, i2 as i32 + 1]; }
            }
        }
        vec![i1 as i32 + 1, i2 as i32 + 1]
    }
}
