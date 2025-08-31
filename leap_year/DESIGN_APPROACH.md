# Leap Year Kata - Design Approach

**Kata Source:** https://www.codurance.com/katas/leap-year

## Solution Overview

Implemented a `LeapYearChecker` class with a single public method `is_leap_year()` that determines if a given year is a leap year.

## Design Decisions

- **Class-based approach**: Encapsulates leap year logic in a dedicated class
- **Private helper methods**: Separated divisibility checks (`__is_divisible_by_4`, `__is_divisible_by_100`, `__is_divisible_by_400`) for readability
- **Sequential rule evaluation**: Implemented the leap year rules in order of precedence

## Algorithm Logic

1. Return `False` if not divisible by 4
2. Return `False` if divisible by 100 but not by 400
3. Return `True` if divisible by 4 or 400

## Testing Strategy

Used parametrized tests covering all leap year scenarios:
- Years not divisible by 4 (e.g., 1997, 1999)
- Regular leap years divisible by 4 (e.g., 1996, 2004)
- Century years divisible by 400 (e.g., 1600, 2000)
- Century years not divisible by 400 (e.g., 1800, 1900)