# Computor V1

## About Polynomial Equations

A **polynomial equation** is a mathematical equation where a variable is raised to various powers and multiplied by coefficients. The general form of a polynomial equation of degree 2 (quadratic) is:

$$ax^2 + bx + c = 0$$

where $a$, $b$, and $c$ are constants (coefficients) and $x$ is the variable. The **roots** or **solutions** of the equation are the values of $x$ that make the equation equal to zero.

Polynomial equations can be:
- **Linear** (degree 1): $ax + b = 0$
- **Quadratic** (degree 2): $ax^2 + bx + c = 0$
- **Higher degree** (degree 3+): $ax^3 + bx^2 + cx + d = 0$, etc.

## Program Purpose

**Computor V1** is a polynomial equation solver that:

1. **Parses** polynomial equations provided as input
2. **Analyzes** the equation to determine its degree
3. **Calculates** the solutions (roots) using appropriate mathematical methods:
   - For quadratic equations: Uses the discriminant formula to find real or complex roots
   - For linear equations: Solves directly
   - Handles degenerate cases and special conditions
4. **Displays** the solutions in a clear, formatted manner

### Running the Program

Execute the program with a polynomial equation as input and it will output all solutions in the real number set (or indicate if solutions exist only in complex numbers).


