func asteroidCollision(asteroids []int) []int {
    stack :=  []int{}
    for _, asteroid := range asteroids {
        for {
            if len(stack) == 0 || asteroid > 0 || (asteroid < 0 && stack[len(stack)-1] < 0) {
                stack = append(stack, asteroid)
                break
            } else {
                sum := stack[len(stack)-1] + asteroid
                if sum > 0 {
                    break
                } else {
                    stack = stack[:len(stack)-1]
                    if sum == 0 {
                        break
                    }
                }
            }
        }
    }
    return stack
}
