# shunting yard algorithm implementation in python

this is an algorithm to convert infix notation to postfix/RPN.

how it works:

1. read the input from left to right
2. if it is a number, add it to the output queue
3. if it is an operator, pop operators from the stack to the output queue until you find an operator with less precedence or a left parenthesis, then push the current operator to the stack
4. if it is a left parenthesis, push it to the stack
5. if it is a right parenthesis, pop operators from the stack to the output queue until you find a left parenthesis, then pop the left parenthesis from the stack and discard it
6. after the input is read, pop any remaining operators from the stack to the output queue
the output queue will contain the expression in postfix/RPN notation.
