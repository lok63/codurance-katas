# Palindrome Radar - Design Approach and Patterns

## Overview

This implementation solves the Palindrome Radar kata using a clean, extensible architecture that separates concerns and provides flexibility for different text preprocessing strategies.

## Core Problem Analysis

The challenge requires detecting palindromes in radar signals while ignoring:
- Case differences
- Punctuation and spaces
- Non-alphanumeric characters

The solution treats this as a two-phase problem:
1. **Text Preprocessing** - Normalize input text
2. **Palindrome Detection** - Check symmetry efficiently

## Design Patterns Used

### 1. Strategy Pattern

**Location**: `src/pre_processors.py`

The preprocessing logic uses the Strategy pattern to allow different text normalization approaches:

```python
class AbstractPreprocessor(ABC):
    @abstractmethod
    def lower_case(self, text: str) -> str: ...
    
    @abstractmethod
    def remove_punctuation(self, text: str) -> str: ...
```

**Benefits**:
- **Extensibility**: Easy to add new preprocessing strategies (e.g., handling different languages)
- **Testability**: Each preprocessor can be tested independently
- **Flexibility**: Runtime selection of preprocessing algorithm

**Implementations**:
- `BasicPreprocessor`: Simple string operations using Python built-ins
- `SpacyPreprocessor`: Advanced NLP-based preprocessing using spaCy

### 2. Dependency Injection

**Location**: `src/palindrome_checker.py:9-10`

```python
class PalindromeChecker:
    def __init__(self, pre_processor: AbstractPreprocessor):
        self.pre_processor = pre_processor
```

**Benefits**:
- **Loose Coupling**: PalindromeChecker doesn't depend on concrete preprocessor implementations
- **Testability**: Easy to inject mock preprocessors for testing
- **Configuration**: Different preprocessing strategies can be used without code changes

### 3. Template Method Pattern

**Location**: `src/pre_processors.py:19-23`

```python
def pre_process(self, word: str) -> str:
    """Apply all preprocessing steps to the input text"""
    text = self.lower_case(word)
    text = self.remove_punctuation(text)
    return text
```

**Benefits**:
- **Consistent Processing**: Ensures same sequence of operations across all preprocessors
- **Extensibility**: Easy to add new preprocessing steps to the pipeline
- **Maintainability**: Single place to modify the preprocessing workflow

## Algorithm Choices

### Palindrome Detection Algorithms

The implementation provides two palindrome detection approaches:

#### 1. Pythonic Approach (`pythonic_palindrome`)
```python
def pythonic_palindrome(word: str) -> bool:
    return word == word[::-1]
```

**Characteristics**:
- **Readability**: Most intuitive and readable
- **Memory**: O(n) - creates reversed string copy
- **Time**: O(n) - always processes entire string

#### 2. Two-Pointer Approach (`efficient_palindrome`)
```python
def efficient_palindrome(word: str) -> bool:
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Characteristics**:
- **Memory**: O(1) - no additional string copies
- **Time**: O(n/2) best case with early termination
- **Efficiency**: Chosen as default for better performance

## Architecture Benefits

### Separation of Concerns
- **PalindromeChecker**: Core palindrome logic
- **Preprocessors**: Text normalization strategies
- **Tests**: Comprehensive coverage of both components

### Single Responsibility Principle
Each class has one clear responsibility:
- `PalindromeChecker`: Palindrome detection
- `BasicPreprocessor`: Simple text preprocessing
- `SpacyPreprocessor`: NLP-based text preprocessing

### Open/Closed Principle
- Open for extension: New preprocessors can be added without modifying existing code
- Closed for modification: Core palindrome logic remains stable

### Liskov Substitution Principle
All preprocessor implementations are interchangeable through the `AbstractPreprocessor` interface.

## Testing Strategy

### Parameterized Testing
```python
@pytest.mark.parametrize("preprocessor_class", [BasicPreprocessor, SpacyPreprocessor])
```

**Benefits**:
- **Coverage**: Same tests run against all preprocessor implementations
- **Consistency**: Ensures all strategies produce equivalent results
- **Maintainability**: Single test suite for multiple implementations

### Comprehensive Test Cases
Tests cover edge cases from the kata requirements:
- Simple palindromes: "anna"
- Mixed case: "Race car"
- With punctuation: "anna!"
- Complex phrases: "A man, a plan, a canal, Panama!"
- False cases: "race car1"

## Extensibility Examples

The design easily accommodates future requirements:

### Adding New Preprocessors
```python
class RegexPreprocessor(AbstractPreprocessor):
    def remove_punctuation(self, text: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]', '', text)
```

### Adding New Detection Algorithms
```python
def recursive_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return recursive_palindrome(word[1:-1])
```

### Language-Specific Preprocessing
The SpacyPreprocessor demonstrates how to integrate advanced NLP capabilities for handling different languages and more sophisticated text normalization.

## Performance Considerations

- **Early Termination**: Two-pointer algorithm stops at first mismatch
- **Memory Efficiency**: Avoid string copying where possible  
- **Preprocessing Choice**: Basic preprocessor for simple cases, SpaCy for complex text

## Conclusion

This implementation demonstrates clean architecture principles while solving the palindrome detection problem efficiently. The use of established design patterns creates a maintainable, testable, and extensible solution that can easily adapt to future requirements.