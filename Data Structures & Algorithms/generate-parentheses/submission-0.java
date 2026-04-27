class Solution {
    // only add open ( if open < n
    // only add close ) if close < open
    // valid/stop when open == close == n

    public void backtrack(int openN, int closeN, int n, List<String> res, Stack<String> stack){
        if (openN == closeN && openN == n){
            String ans = String.join("",stack);
            res.add(ans);
            return;
        }

        if (openN < n){
            stack.push("(");
            backtrack(openN+1, closeN,n, res, stack);
            stack.pop();
        }

        if (closeN < openN){
            stack.push(")");
            backtrack(openN, closeN+1, n, res, stack);
            stack.pop();
        }
    } 

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        Stack<String> stack = new Stack<>();
        backtrack(0, 0, n, res, stack);
        return res;
    }
}
