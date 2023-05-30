import numpy as np
from numpy import random
import math

class node:
    def __init__(self,board,strength_node_storage,ai_player=1,depth=0,children=None,parent=None,make_children=1):
        # self.is_board_valid()
        self.board = board
        self.player = 3 - self.whos_turn()
        self.ai_player = ai_player
        self.opponent = 3 - self.player
        self.depth = depth
        self.turn = self.whos_turn()
        self.board_state = None
        self.children = None
        self.parent = parent
        self.strength_node_storage = strength_node_storage
        self.winstate()
        self.valid_board = self.is_board_valid()


        if self.player == self.turn:
            raise Exception(f"Not valid turn for {self.player} on board: {self.board}")

        # if self.board_state != None:
        #     print(self.board,self.board_state)

        # if self.depth == 1:
        #     print(printable_board(self.board),self.depth,self.board_state,sep="\n")

        if self.board_state == None and make_children !=0 and self.is_board_valid:
            self.generate_children(depth=(self.depth+1))
        
        if self.board_state != None:
            self.strength_node_storage.append(self.board_state)
            # if self.board_state <= 0:
            #     print(printable_board(self.board),self.board_state,self.player,sep="\n")
        
        # self.strength = self.find_strength()

    def find_availible_spaces(self):
        self.availible_spaces = []
        for index,position in enumerate(self.board):
            if position == 0:
                self.availible_spaces.append(index)
            else:
                self.availible_spaces == None
        return self.availible_spaces
    
    #PLace whatever winstate and weights in this function. Initially made for tic-tac-toe
    def winstate(self):
            winning_states = [
                [0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]
            ]
            for win_state in winning_states:
                if self.board[win_state[0]] == self.board[win_state[1]] == self.board[win_state[2]] and (self.board[win_state[0]] == (self.ai_player)):
                    self.board_state = 1000
                    # (5**-(self.depth/10)-2)
                    # -(5**-(self.depth-10))
                    return self.board_state
                if self.board[win_state[0]] == self.board[win_state[1]] == self.board[win_state[2]] and (self.board[win_state[0]] == (3-self.ai_player)):
                    self.board_state = -1*self.depth
                    # -(5**-(self.depth/10)-2)
                    return self.board_state
                if self.board.count(0) == None:
                    self.board_state = 0
                    # (5**-(self.depth/10)-2)
                    return self.board_state
            self.board_state = None

            if self.board_state != None:
                self.strength_node_storage.append(self.board_state)

            return self.board_state
    
    def move(self,position,player=1):
        new_board = []
        for index in self.board:
            new_board.append(index)
        new_board[position] = player
        return new_board

    def is_board_valid(self):
        if self.winstate() == None\
        and self.board.count(1) >= self.board.count(2):
            return True
        elif self.winstate() == 1\
        and self.board.count(1) > self.board.count(2):
            return True
        elif self.winstate() == -1\
        or self.winstate() == 0\
        and self.board.count(1) == self.board.count(2):
            return True
        else:
            raise Exception("Error:Invalid board")

    def whos_turn(self):      
        #count the number of each.
        if self.board.count(1) > self.board.count(2):
            self.turn = 2
        elif self.board.count(1) == self.board.count(2):
            self.turn = 1
        else:
            self.turn = 1
        return self.turn        

    def generate_children(self,depth=0):
        """
        Generates all possible boards from the node's currrent board. Creates additional nodes with all possible boards.
        Loads all the node objects into the child list.
        """
        if self.children == None:
            self.children = []
        for space in self.find_availible_spaces():
            self.children.append(node(self.move(space,self.whos_turn()),self.strength_node_storage,depth=depth,ai_player=self.ai_player))
        # print(self.board)
        # print(self.board," Parent ------------")
        # for child in self.children:
        #     print(child.board,f"Weigth:{child.board_state}",f"Depth:{child.depth}")
        # print('\n')
        if self.children == []:
            self.children = None
        return self.children
    
    def is_board_valid(self):
        x_moves = self.board.count(1)
        o_moves = self.board.count(2)
        if self.winstate() == None\
        and x_moves >= o_moves:
            return True
        elif self.winstate() == 1\
        and x_moves > o_moves:
            return True
        elif self.winstate() == -1\
        or self.winstate() == 0\
        and x_moves == o_moves:
            return True
        else:
            return False
