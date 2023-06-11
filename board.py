"""The board class."""

class Board(object):

    def __init__(self):
        self.board = [[' ' for x in range(3)] for y in range(3)]
