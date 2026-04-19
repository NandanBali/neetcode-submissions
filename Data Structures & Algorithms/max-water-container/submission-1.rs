impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut max_area: i32 = 0;
        let mut l1: usize = 0;
        let mut l2: usize = heights.len() - 1;

        while l2 > l1 {
            let min_i = if heights[l1] > heights[l2] { l2 } else { l1 };
            let area = (l2 - l1) as i32 * heights[min_i];
            if area > max_area { max_area = area; }
            if heights[l1] < heights[l2] {
                l1 += 1;
            } else {
                l2 -= 1;
            }
        }

        max_area
    }
}
