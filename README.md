# Digite Infotech Private Limited Assignment

This document outlines the solutions to the coding challenges presented by Digite Infotech Private Limited. The solutions are implemented in Python.

**1. Given two numbers a, b where b > a, find the sum of all primes between them.**

This problem involves finding the sum of all prime numbers that lie between two given integers, `a` and `b`, where `b` is strictly greater than `a`.

**Approach:**

1. **Input:** Obtain the values of `a` and `b` from the user.
2. **Validation:** Ensure that `b` is indeed greater than `a`. If not, raise an appropriate error.
3. **Prime Number Check:** Implement a function `is_prime(n)` to efficiently determine if a number `n` is prime. This can be optimized by checking divisibility only up to the square root of `n`.
4. **Summation:** Iterate through the range of numbers from `a` to `b`. For each number, check if it's prime using the `is_prime()` function. If it's prime, add it to the running sum.
5. **Output:** Display the calculated sum of all prime numbers between `a` and `b`.

![sumOfPrime](https://github.com/user-attachments/assets/2ff1c3da-3d85-4834-a0c8-fcab694994c7)

***3. Find the 3rd smallest number in an array.***

This problem involves finding the third-smallest number within an array of integers.

**Approach:**

1. **Input:** Obtain the array of integers from the user.
2. **Sorting:** Sort the array in ascending order. You can use a suitable sorting algorithm like Selection Sort, Insertion Sort, or a more efficient algorithm like Merge Sort or Quick Sort.
3. **Output:** Display the third-smallest number.

![thridSmallestElement](https://github.com/user-attachments/assets/9120fbd0-5033-4cac-8912-154bba6f314b)

