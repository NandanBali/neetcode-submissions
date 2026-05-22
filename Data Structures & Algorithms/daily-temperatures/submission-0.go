func dailyTemperatures(temperatures []int) []int {
    htStack, res := []int{}, []int{}
    for _, temp := range temperatures {
        res = append(res, 0)
        // htStack
        idx := len(htStack)
        zc := 0
        for i := 1; i <= idx; i++ {
            // keep popping until 
            if htStack[idx-i] < temp {
                htStack = htStack[:idx-i]
                zc++
            } else {
                break
            }
        }
        htStack = append(htStack, temp)
        r := len(res) - 1
        for i := 0; i < zc; i++ {
            for  {
               r -= 1
               if res[r] == 0 {
                    res[r] = len(res) - r - 1
                    break
               }
            }
        }
    }

    return res
}
