Quadratic Solver - Python

Solves ax² + bx + c = 0 - built entirely on mobile (Pydroid 3)

Features
Handles real and complex roots
Input validation (no crash on letters or empty input)
Prevents a=0 (not quadratic)
Clean formatted output
Loop to solve multiple equations

How it works
Uses cmath.sqrt() so negative discriminants return complex numbers.

Formula:
D = b² - 4ac
x = (-b ± √D) / 2a

How to Run
python quadratic_solver.py

Example
Enter a: 1
Enter b: -3
Enter c: 2
Solving: 1.0x² + -3.0x + 2.0 = 0
Discriminant = 1.0
Result: Two distinct real roots
x1 = 2
x2 = 1

Built With
Python 3 + cmath
Pydroid 3 (Android)

Author
Ayodeji Lucas - learning Python on mobile
---
