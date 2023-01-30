"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == X:
                countX+=1
            if board[row][column] == O: 
                countO+=1

    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY :
                allPossibleActions.add((row, column))
    
    return allPossibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("not valid action")
    
    row, column = action 
    board_copy = copy.deepcopy(board)
    board_copy[row][column] = player(board)

    return board_copy


def checkRow(board, player):

    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        
    return False

def checkColumn(board, player):

    for column in range(len(board)):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
        
    return False

def checkFirstDig(board, player):
    count = 0

    for row in range(len(board)):
        for column in range(len(board[row])):
            if row == column and board[row][column]==player:
                count += 1
    
    if count == 3:
        return True
    else: 
        return False

def checkSecondDig(board, player):
    count = 0

    for row in range(len(board)):
        for column in range(len(board[row])):
            if (len(board)-1-row) == column and board[row][column]==player:
                count += 1
    
    if count == 3:
        return True
    else: 
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkColumn(board, X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    elif checkRow(board, O) or checkColumn(board, O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
        
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column]==EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v= -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    v= math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
        plays = []

        for action in actions(board):

            plays.append([min_value(result(board,action)), action])
        
        return sorted(plays, key= lambda x: x[0], reverse=True)[0][1]
    elif player(board)==O:
        plays = []

        for action in actions(board):

            plays.append([max_value(result(board,action)), action])
        
        return sorted(plays, key= lambda x: x[0])[0][1]
