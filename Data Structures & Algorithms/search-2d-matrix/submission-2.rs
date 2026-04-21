impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        use std::cmp::Ordering;
        
        // binary search on rows
        let mut low_r: usize = 0;
        let mut high_r: usize = matrix.len() - 1;
        let row_size = matrix[0].len();
        let cols = matrix.len() - 1;
        if target > matrix[cols][row_size-1] {
            return false;
        }

        if target < matrix[0][0] {
            return false;
        }

        while low_r <= high_r {
            let mid = low_r + (high_r - low_r) / 2;
            match matrix[mid][0].cmp(&target) {
                Ordering::Greater => {
                    high_r = mid - 1;
                },
                Ordering::Less => {
                    low_r = mid + 1;
                },
                Ordering::Equal => {
                    return true;
                }
            }
        }

        let mut l = 0;
        let mut h = row_size - 1;

        let lr = if low_r == 0 {  low_r } else {  low_r - 1 };

        while l <= h {
            let mid = l + (h-l) / 2;
            match matrix[lr][mid].cmp(&target) {
                Ordering::Less => {
                    l = mid + 1;
                },
                Ordering::Equal => {
                    return true;
                },
                Ordering::Greater => {
                    h = mid - 1;
                }
            }
        }

        false
    }
}
