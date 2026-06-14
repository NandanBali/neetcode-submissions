use std::collections::BinaryHeap;

impl Solution {
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        let mut heap = BinaryHeap::new();

        if a > 0 { heap.push((a, 'a')); }
        if b > 0 { heap.push((b, 'b')); }
        if c > 0 { heap.push((c, 'c')); }

        let mut result = String::new();

        while let Some((count, ch)) = heap.pop() {
            let bytes = result.as_bytes();
            let len = bytes.len();

            // Would adding ch make 3 in a row?
            if len >= 2 && bytes[len - 1] == ch as u8 && bytes[len - 2] == ch as u8 {
                match heap.pop() {
                    Some((count2, ch2)) => {
                        result.push(ch2);
                        if count2 > 1 {
                            heap.push((count2 - 1, ch2));
                        }
                        heap.push((count, ch)); // put ch back
                    }
                    None => break,
                }
                continue;
            }

            // Add 2 if it's safe and beneficial, otherwise 1
            let last_is_same = len >= 1 && bytes[len - 1] == ch as u8;
            let count_to_add = if !last_is_same && count > 1 { 2 } else { 1 };

            for _ in 0..count_to_add {
                result.push(ch);
            }

            if count > count_to_add {
                heap.push((count - count_to_add, ch));
            }
        }

        result
    }
}
