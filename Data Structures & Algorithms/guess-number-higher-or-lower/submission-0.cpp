/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int x_l = 0;
        int x_h = n;

        while (x_h > x_l) {
            int x_m = x_l + (x_h - x_l) / 2;
            int g = guess(x_m);
            if (g == 0) {
                return x_m;
            } else if (g == 1) {
                x_l = x_m + 1;
            } else {
                x_h = x_m - 1;
            }
        }
        return x_l;
   }
};