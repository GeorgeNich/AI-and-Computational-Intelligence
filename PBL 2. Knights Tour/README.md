# The Knight's Tour
![Knight's Tour GUI](knight_tour_demo.gif)

### Overview

This repository contains a Python program that solves the Knight's Tour problem on an `n x n` chessboard. The Knight's Tour problem is a classic chess puzzle where the goal is to find a sequence of moves for a knight such that it visits every square on the board exactly once.

### Features

- Interactive GUI for visualizing the Knight's Tour on the chessboard.
- Efficient backtracking algorithm to find a valid solution.
- Detailed report explaining the algorithm and performance analysis.

### Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)
- (Optional) [Virtual environment](https://docs.python.org/3/tutorial/venv.html) for isolating dependencies

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/GeorgeNich/AI-and-Computational-Intelligence.git
   cd AI-and-Computational-Intelligence/PBL2.%20Knights%20Tour/
   
2. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate

4. Install dependencies
   ```bash
    pip install -r requirements.txt

---

## Usage

1. Run the program:
    ```bash
    python knight_GUI.py

2. Enter the value of n (the size of the chessboard). Ensure that n is greater than 4, as the Knight's Tour problem is meaningful for larger boards.

3. The GUI will display the knight's moves on the chessboard, and you can watch the solution unfold.

4. Once the tour is completed, the program will display a message with the time taken to solve the tour.

## Code Structure

- 'knight_GUI.py': The main Python script for solving and visualizing the Knight's Tour problem.
- 'PBL2 The Knights Tour report.pdf': A detailed report explaining the algorithm, code structure, and performance analysis.

## Acknowledgments
This project's solution references the Knight's Tour algorithm as explained on [GeeksforGeeks](https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/). We are grateful for the comprehensive resources and explanations provided, which significantly aided in understanding and implementing the Warnsdorff's algorithm for the Knight's Tour problem.

## License
This project is licensed under the [MIT License](LICENSE).

