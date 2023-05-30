from bfs_experiment3 import *

board_grid = {
    "7": 0,
    "8": 1,
    "9": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "1": 6,
    "2": 7,
    "3": 8,
}


def initialize_board():
    board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return board_state


def printable_board(board):
    ascii_board = []
    for space in board:
        if space == 0:
            ascii_board.append("   ")
        elif space == 1:
            ascii_board.append(" X ")
        elif space == 2:
            ascii_board.append(" O ")
        else:
            raise ValueError
    formatted_board = f"""
                            1   2   3\n
                        A  {ascii_board[0]}|{ascii_board[1]}|{ascii_board[2]}
                           ---+---+---
                        B  {ascii_board[3]}|{ascii_board[4]}|{ascii_board[5]}
                           ---+---+---
                        C  {ascii_board[6]}|{ascii_board[7]}|{ascii_board[8]}"""
    return formatted_board


def whos_turn(board):
    x_moves = [space for space in board if space == 1]
    o_moves = [space for space in board if space == 2]
    if len(x_moves) == len(o_moves):
        return 1
    elif len(x_moves) > len(o_moves):
        return 2
    else:
        raise ValueError


def is_move_valid(board, player, location):
    if did_player_win(board, 1) == False and did_player_win(board, 2) == False:
        if board[location] == 0 and whos_turn(board) == player:
            return True
        else:
            return False


def move_external(board, player, location):
    if is_move_valid(board, player, location) == True:
        if player == 1:
            board[location] = 1
        if player == 2:
            board[location] = 2
        return board
    else:
        return []


def did_player_win(board, player):
    if (
        board[0] == board[3] == board[6]
        and board[0] == player
        or board[0] == board[1] == board[2]
        and board[0] == player
        or board[0] == board[4] == board[8]
        and board[0] == player
        or board[1] == board[4] == board[7]
        and board[1] == player
        or board[2] == board[4] == board[6]
        and board[2] == player
        or board[2] == board[5] == board[8]
        and board[2] == player
        or board[3] == board[4] == board[5]
        and board[3] == player
        or board[6] == board[7] == board[8]
        and board[6] == player
    ):
        return True
    else:
        return False

def ai(board,player):
    def find_availible_spaces(board):
            availible_spaces = []
            for index,position in enumerate(board):
                if position == 0:
                    availible_spaces.append(index)
                else:
                    availible_spaces == None
            return availible_spaces

    def internal_move(board,player,location):
        temp_board = board[:] 
        if is_move_valid(temp_board, player, location) == True:
            if player == 1:
                temp_board[location] = 1
            if player == 2:
                temp_board[location] = 2
            return temp_board
        else:
            return []
        
    def terminal_node_strengths(board_list, player):
        strength = []
        myNode = node(board_list, strength, ai_player=player)

        del(myNode)
        if strength == []:
            return 0
        
        weighted_min = np.average(strength)
        
        return weighted_min

    def evaluate_moves(board,player):
        new_boards = {}
        availible_move = find_availible_spaces(board)
        for moves in availible_move:
            new_boards[moves] = internal_move(board,player,moves)
            if new_boards[moves] == []:
                raise Exception("No valid moves for this position.")

        evaluated_moves = {}
        for position in new_boards:
            position = position
            evaluated_moves[position] = terminal_node_strengths(new_boards[position],player)
        # print(evaluated_moves)
        return evaluated_moves

    def pick_move(board,player):
        strengths = evaluate_moves(board,player)
        max = -10000000000
        print(strengths)
        for position in strengths:
            if strengths[position] >= max:
                max = strengths[position]
                max_key = position
        return [board, player, max_key,strengths]
    
    move_choice = pick_move(board,player)
    return move_choice

def player_play_game():
    board_state = initialize_board()
    print(printable_board(board_state))
    while did_player_win(board_state, 1) != True and did_player_win(board_state, 2) != True:
        while True:
            try:
                player = whos_turn(board_state)
                next_move = board_grid[input(f"What spot do you want, {player}?")]
                break
            except KeyError or is_move_valid(board_state, player, next_move) == False:
                print("Invalid move, try again")
        new_board = move_external(board_state, player, next_move)
        print(printable_board(new_board))
    print(f"{player} wins!")

def player_vs_ai(human_turn):
    board_state = [0,0,0,0,0,0,0,0,0]
    player = whos_turn(board_state)
    numbers_to_player = {
        1:'X',
        2:'O'
    }
    x_wins = did_player_win(board_state, 1)
    o_wins = did_player_win(board_state, 2)
    print(printable_board(board_state))
    while did_player_win(board_state, 1) != True and did_player_win(board_state, 2) != True:
        player = whos_turn(board_state)
        if human_turn == whos_turn(board_state):
                try:
                    next_move = board_grid[input(f"What spot do you want, {numbers_to_player[human_turn]}?")]
                except KeyError or is_move_valid(board_state, numbers_to_player[human_turn], next_move) == False:
                    print("Invalid move, try again")
        else:
            ai_move = ai(board_state, 3 - human_turn)
            next_move = ai_move[2]
        new_board = move_external(board_state, player, next_move)
        print(printable_board(new_board))
    print(f"{numbers_to_player[human_turn]} wins!")


def main():
    player_vs_ai(1)
main()
