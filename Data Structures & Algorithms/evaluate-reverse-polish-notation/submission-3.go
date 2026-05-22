func evalRPN(tokens []string) int {
    stack := []int{}
    for _, token := range tokens {
        switch token {
            case "+", "-", "*", "/":
                r1 := stack[len(stack)-1]
                r2 := stack[len(stack)-2]
                stack = stack[:len(stack)-2]
                switch token {
                    case "+":
                        stack = append(stack, r2+r1)
                    case "-":
                        stack = append(stack, r2-r1)
                    case "*":
                        stack = append(stack, r2 * r1)
                    case "/":
                        stack = append(stack, r2 / r1)
                }
            default:
                n, _ := strconv.Atoi(token)
                stack = append(stack, n)
        }
    }

    return stack[0]
}
