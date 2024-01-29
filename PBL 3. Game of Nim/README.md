# Nim Game

## Introduction
Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps or piles. This Python project implements the Nim game, featuring an AI opponent using the Minimax algorithm with Alpha-Beta pruning.

## Installation
To play the Nim game, Python needs to be installed on your computer. Download and install Python from [here](https://www.python.org/downloads/).

## Usage
To play the game, follow these steps:
1. Clone the repository or download the source code.
2. Navigate to the directory containing the game files.
3. Run the game using a Python interpreter:

    ```bash
      python main.py

## Game Files
- [Game Report (PDF)](PBL%203%20The%20Game%20of%20Nim%20report.pdf) - Detailed report on the project.
- [main.py](main.py) - Main Python script for the game.
- [soloution.py](soloution.py) - Python script containing the Minimax algorithm for the game.

## Features
- Interactive player input for game moves.
- AI opponent using the Minimax algorithm.
- Configurable number of piles and objects.
- Command-line interface for easy gameplay.

## Game Rules
- The game starts with a number of piles of objects.
- Players take turns removing any number of objects from one of the piles.
- The player forced to remove the last object loses.

## How to Play
The objective of Nim is to avoid taking the last object.

### Making a Move
- Each move requires entering two numbers: the number of objects to remove, and the index of the pile you are taking them from.
- The piles are indexed starting from 0.
- For example, to remove one object from the second pile, enter `1 1`. This means "remove 1 object from pile index 1".

### Gameplay
1. When prompted, enter your move in the format `number_of_objects pile_index`. For instance, `1 1` to remove one object from the second pile.
2. After your move, the AI will make its move.
3. The game continues with each player alternately removing objects from piles.
4. The player who is forced to take the last object loses.

Remember, the strategy is not just about the number of objects you take, but also from which pile you take them.


