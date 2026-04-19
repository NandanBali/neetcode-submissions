impl Solution {
    pub fn num_rescue_boats(p: Vec<i32>, limit: i32) -> i32 {
       let mut people = p.clone();
       let mut res = 0;
       
        people.sort_unstable();
        let mut p1 = 0;
        let mut p2 = people.len() - 1;
        while p2 > p1 {
            let sum = people[p1] + people[p2];
            if sum > limit {
                res += 1;
                p2 -= 1;
            } else {
                res += 1;
                p2 -= 1;
                p1 += 1;
            }
        }

        if p1 == p2 {
            res += 1;
        }
        res
    }
}
