# TicTacToeAI
A very simple breadth first search algorithm applied to a game of tic tac toe.

How to Play
Download both files and place them into the same directory location. Then run execute the GameLogic function. The file will then start producing an ascii board to play with. At the end of each turn that the search algorithm makes it will produce the strength for each possible position on the board.

File Descriptions
The NodeObject file creates node objects which are possible board game states. This object has multiple functions and is the core of the bfs algorithm.
The GameLogic file is the game itself. This file manages the node objects to search for the most optimal move to make.

Areas for Improvement
The search algorithm is severly lacking in optimization. The main issue is the inclusion of recency bias within the strenghts. The code will avoid short term losses and ignore long term losses.
