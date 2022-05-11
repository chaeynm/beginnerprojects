# credits to kylie ying
import random

class Board:
    def __init__(self, board_size, num_bombs):
        self.board_size = board_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.num_bombs = num_bombs
        # initialise to keep track
        self.dug = set()
        self.assign_values_to_board()

    def make_new_board(self):
        # generate new board

        board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        bombs_planted = 0

        # use while loop because we don't want to be iterated
        while bombs_planted < self.num_bombs:
            location = random.randint(0, self.board_size**2-1)
            row = location // self.board_size
            column = location % self.board_size

            if board[row][column] == '*':
                # we already have planted bombs
                continue

            board[row][column] = '*'
            bombs_planted += 1
    def assign_values_to_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c]=='*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)
    def get_num_neighboring_bombs(self,row,columns):
        # check all the numbers around bombs
        # make sure that it doesn't go out of bounds

        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.board_size-1, row+1) + 1):
            for c in range(columns-1, (columns-1)+1):
                if r == row and c == columns:
                    continue

                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

#play the game
def play(board_size = 10, num_bombs = 0):
    # create board&plant bombs
    pass

