# Recursion

This chapter talks about recursion.

### The call stack with recursion

Recursive functions use the call stack too! Let’s look at this in action 
with the factorial function. factorial(5) is written as 5!, and it’s 
defined like this: 5! = 5 * 4 * 3 * 2 * 1. Similarly, factorial(3) is 
3 * 2 * 1. Here’s a recursive function to calculate the factorial of a 
number:

```
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
```

Now you call fact(3). Let’s step through this call line by line and see 
how the stack changes. Remember, the topmost box in the stack tells 
you what call to fact you’re currently on.

## Recap

- Recursion is when a function calls itself.
- Every recursive function has two cases: the base case and the recursive case.
- A stack has two operations: push and pop.
- All function calls go onto the call stack.
- The call stack can get very large, which takes up a lot of memory.