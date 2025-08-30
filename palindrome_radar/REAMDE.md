# Palindrome Radar
Codurance link: https://www.codurance.com/katas/palindrome-radar

## Summary
NASA’s latest radar technology captures shape signatures of flying objects as strings of characters. As everyone knows, UFO’s are shaped like saucers and are therefore symmetrical. If a radar signal string is a Palindrome then it is symmetrical and represents a UFO. A palindrome is a word, phrase, number, or sequence of characters that reads the same forwards and backwards.


## Your Task
Implement a function that accepts a radar signal string and if it is symmetrical in shape determines that it is a UFO, otherwise it is not. If the string is a Palindrome then it is deemed symmetrical.

## Input
A string representing the radar signal for the object. Ignore spaces, punctuation and differences in letter case.

## Output
Return True if the input string is a Palindrome and therefore represents a UFO signature, False otherwise.

## Rules
Ignore capital letters, punctuation, and word dividers. Any character other than alphanumeric characters are classed as punctuation. Numbers in the radar signal should be treat as strings.

## Examples
1. "anna" => True
2. "anna!" => True
3. "race car" => True
4. "race car1" => False
5. "Race car" => True
6. "A man, a plan, a canal, Panama!" => True
7. "axDbTbd6" => False
8. "6axDbTbd6" => True
9. "Hello, World!" => False