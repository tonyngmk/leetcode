### 1. Sliding Window

- Time : $O(n \times (m \times i))$, where $n$ is the length of long string, m is the amount of words, and i is the length of each word.
- Space : $O(1)$, no extra space required except for answer.

### 2. Hash set

- Time : $O(n \times (m \times i))$, where $n$ is the length of long string, m is the amount of words, and i is the length of each word.
- Space : $O(m \times i)$, where we hash the given word list

### 3. Trie

- Time: $O(n \times s + m^2)$, where:
    - m denote text.length, 
    - n denote words.length, and 
    - s as the average length of the words

- Space: $O(n \times s)$

