# Europa Exploration Mission

This is a navigation module simulation for NASA's mission to Europa, one of Jupiter's moons. Some robots are deployed on a rectangular plateau and instructed to move based on user input. Each robot receives an initial position and a string of commands ('L', 'R', 'M') to navigate the surface.

---
## Problem Overview

- The plateau is a rectangular grid defined by upper-right coordinates (lower-left is always '0 0).
- Each robot is given:
  - A starting position: 'x y D' (where D is direction: 'N', 'E', 'S', or 'W'')
  - A sequence of instructions: a string containing the characters 'L', 'R', and 'M'
    - 'L': turn left 90°
    - 'R': turn right 90°
    - 'M': move one grid unit forward in the current direction
- Robots are processed **sequentially**; no collision detection is required.
- If a robot attempts to move outside the plateau bounds, it will ignore that move and remain in place.

---

## Assumptions

1. **Plateau bounds** are defined by user input as a single line like:  
   '5 5'
   - Lower-left corner is at '(0, 0)'
2. **Robots' input** is taken interactively:
   - First line: Initial position (e.g., '1 2 N')
   - Second line: Instructions (e.g., 'LMLMLMLMM')
   - Press 'Enter' with no input to stop entering robots
3. **Invalid inputs** (e.g., incorrect direction, non-positive and non-integer coordinates, invalid instructions) will prompt the user again.
4. Robot retains its last valid position if movement leads it to go beyong the plateau bounds - a blocking message is sent.
5. Direction and instruction characters are case-insensitive ('lrm', 'LRM' are valid).

---

## Input and Output 

### Test Input:
```text
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Expected Output:
```text
1 3 N
5 1 E
```

## To Run

### Requirements
- Python 3.7+

### Running the Script
- python3 nasa.py
- python3 test_nasa.py (To run the test cases for the main code)
