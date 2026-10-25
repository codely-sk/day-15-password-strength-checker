# Day 15 — Password Strength Checker

## About the Project
This is Day 15 of my Project 20 Python challenge. This program checks a password against five basic criteria and suggests ways to improve it.

## Features
- Checks minimum password length.
- Checks for uppercase and lowercase letters.
- Checks for numbers and special characters.
- Calculates a simple strength score.
- Provides suggestions for missing criteria.

## Python Concepts Learned
- Functions and parameters
- `any()` and generator expressions
- String methods: `isupper()`, `islower()`, `isdigit()`, and `isalnum()`
- Lists and `append()`
- Conditions and scoring systems
- Returning multiple values
- Multiple assignment (unpacking)

## How It Works
1. The user enters a password.
2. The program checks five criteria.
3. Each satisfied criterion adds one point.
4. The score determines a Weak, Moderate, or Strong rating.
5. The program displays suggestions for criteria that were not met.

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Run `password_checker.py`.
4. Enter a test password when prompted.

## What I Learned
- How to check individual characters in a string.
- How `any()` works with a generator expression.
- How a function can return multiple values.
- How to use a score to classify results.
- How to give users helpful feedback.

## Note
This is a beginner learning project. Its rating is based on five basic checks and does not guarantee that a password is secure. Do not enter real passwords into the program.

## Project 20
Part of my 20-day Python project challenge to improve my coding logic and build independent programming skills.