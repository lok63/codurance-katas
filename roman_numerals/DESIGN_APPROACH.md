# Roman Numerals Kata - Design Approach

[Codurance Link
](https://www.codurance.com/katas/roman-numerals)
## Problem Overview

The Roman Numerals kata requires converting decimal numbers to their Roman numeral representation. This seemingly simple problem contains several subtle challenges that make it an excellent exercise in algorithmic thinking.

## Key Challenges

### 1. Subtraction Cases
The most significant challenge is handling the subtraction notation where smaller numerals precede larger ones:
- IV (4) instead of IIII
- IX (9) instead of VIIII
- XL (40) instead of XXXX
- XC (90) instead of LXXXX
- CD (400) instead of CCCC
- CM (900) instead of DCCCC

### 2. Greedy Algorithm Consideration
Roman numerals follow a greedy approach - we should always use the largest possible numeral first. However, this requires careful consideration of subtraction cases.

### 3. State Management
Early implementations might use instance variables that persist between method calls, leading to incorrect results on subsequent conversions.

## Solution Design

### Core Algorithm: Greedy with Predefined Mappings

The solution uses a greedy algorithm with a carefully ordered list of value-numeral pairs:

```python
values = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
```

### Why This Works

1. **Ordered by Descending Value**: We process largest values first
2. **Includes Subtraction Cases**: By explicitly including pairs like (900, "CM"), we handle subtraction notation naturally
3. **Greedy Processing**: For each value, we use as many instances as possible before moving to the next

### Algorithm Steps

1. Start with the input number
2. For each value-numeral pair (in descending order):
   - Calculate how many times this value fits into the remaining number
   - Add that many instances of the numeral to the result
   - Subtract the used amount from the remaining number
3. Continue until the number reaches zero

## Edge Cases Handled

- **Single digits**: 1→I, 5→V, etc.
- **Subtraction cases**: 4→IV, 9→IX, 40→XL, 90→XC, 400→CD, 900→CM
- **Complex numbers**: 1994→MCMXCIV (combines multiple subtraction cases)
- **Large numbers**: 1000→M, 2000→MM, etc.

## Alternative Approaches Considered

### 1. Recursive Decomposition
Breaking numbers into units, tens, hundreds, etc., and handling each place separately. This approach is more complex and doesn't handle subtraction cases as elegantly.

### 2. Rule-Based Matching
Using pattern matching or conditional logic for each case. This leads to verbose, hard-to-maintain code with many special cases.

### 3. Mathematical Modular Approach
The original flawed implementation attempted to use modular arithmetic to determine remainders. This approach struggled with subtraction cases and state management.

## Why the Chosen Approach is Superior

1. **Simplicity**: Single loop with clear logic
2. **Completeness**: Handles all cases including subtraction notation
3. **Maintainability**: Adding new mappings (if needed) is trivial
4. **Performance**: O(1) time complexity for practical inputs
5. **Stateless**: No side effects or persistent state between calls

## Testing Strategy

The test suite covers:
- Basic single numerals (1, 5, 10, 50, 100, 500, 1000)
- Simple additions (2→II, 3→III, etc.)
- Subtraction cases (4→IV, 9→IX, 40→XL, 90→XC, 400→CD, 900→CM)
- Complex combinations (1994→MCMXCIV)

## Conclusion

The key insight is recognising that Roman numerals follow a greedy algorithm pattern, but the subtraction cases must be treated as atomic units rather than decomposed further. By including these cases in our value mappings, the algorithm naturally produces correct results without special case handling.