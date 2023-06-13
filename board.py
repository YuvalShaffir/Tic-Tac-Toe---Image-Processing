"""The board class."""
import numpy as np

# Constants
class Score():
    """Score class to represent the score of the game."""
    X = 1
    O = -1
    TIE = 0


class Board(object):


    def __init__(self):
        # initiate an empty 3x3 board
        self.board = np.empty((3, 3), dtype=str)

    def get_board(self):
        """Returns the board."""
        return self.board

    def set_board(self, board):
        """Sets the board."""
        self.board = board

    def check_winner(self):
        """Checks if there is a winner.
           Returns the sign of the winner, NULL if there is no winner."""

        # horizontal
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

        # vertical
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        # diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return NULL

    def minimax(self, depth, is_max):
        """Minimax algorithm.
        @param depth: the depth of the tree
        @param is_max: boolean to indicate if it's the max player's turn
        @return: the best score for that player
        """
        # check if someone won
        res = self.check_winner()
        if res != NULL:
            return res

        # if it's the max player's turn (ai_player)
        if is_max:
            best_score = float('-inf') # -infinity
            # check all possible empty spots
            for i in range(3):
                for j in range(3):
                    # is the spot empty?
                    if self.board[i][j] == '':
                        self.board[i][j] = ai_player # set the board spot with ai's sign
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = '' # reset the board spot to empty

                        if score > best_score:
                            best_score = score

            return best_score

        # if it's the min player's turn
        else:
            best_score = float('inf')  # infinity
            # check all possible empty spots
            for i in range(3):
                for j in range(3):
                    # is the spot empty?
                    if self.board[i][j] == '':
                        self.board[i][j] = human_player  # set the board spot with human's sign
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ''  # reset the board spot to empty

                        if score > best_score:
                            best_score = score

            return best_score

def ai_player_sign(human_player):
    """Returns the sign of the ai player."""
    if human_player == 'X':
        return 'O'
    else:
        return 'X'

def test_game_setup():
    """Test the game setup."""
    board = Board()
    paint_board(board.get_board())

def paint_board(board):
    print(" " + board[0][0] + "  |  " + board[0][1] + " |  " + board[0][2])
    print("---+---+---")
    print(" " + board[1][0] + "  |  " + board[1][1] + " |  " + board[1][2])
    print("---+---+---")
    print(" " + board[2][0] + "  |  " + board[2][1] + " |  " + board[2][2])


if __name__ == '__main__':
    human_player = 'O'
    ai_player = ai_player_sign(human_player)
    current_player = human_player
    test_game_setup()