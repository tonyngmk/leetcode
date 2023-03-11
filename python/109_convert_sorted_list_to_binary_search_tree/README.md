## 1. Recursion

- Time: O(n log n)
    - Since we have to iterate through a balanced tree and calculate the middle element, this may appear as $O(n^2)$.
    - However, the first step is actually $\frac{N}{2}$, second step is $2\times\frac{N}{4}$, third step is $3\times\frac{N}{8}$, etc.
    
- Space: O(log n)
    - Since we have to construct a balanced tree, it is bounded by O(log n) of the recursion stack

## 2. Recursion + Coversion to Array

- Time: O(log n)
    - Only requires the act of bisecting of array

- Space: O(n)
    - Additional array required