impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut high: i32 = *piles.iter().max().unwrap();
        let mut low: i32 = 1;

        while low < high {
            let k: i32 = low + (high - low) / 2;
            let r1 = Self::check_koko(&piles, low, h);
            let r2 = Self::check_koko(&piles, k, h);

            if r1 {
                return low;
            } else if !r1 && r2 {
                low += 1;
                high = k;
            } else if !r1 && !r2 {
                low = k+1;
            }
        }

        low
    }

    fn check_koko(p: &[i32], n: i32, t: i32) -> bool {
        let mut total_hours: i64 = 0;
        for i in p.iter() {
            total_hours += (i / n) as i64;
            if i % n != 0 {
                total_hours += 1;
            }
        }
        total_hours <= t as i64
    }  
}
