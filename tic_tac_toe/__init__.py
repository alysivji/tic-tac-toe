"""Tic-Tac-Toe Game"""

NUM_ROWS = 3
NUM_COLS = 3
SEPARATOR = '---|---|---\n'


class Board:
    """The board is made up of squares, stored as a mapping"""

    def __init__(self):
        """Set up board"""

        board = {}
        position_counter = 1

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                board[position_counter] = position_counter
                position_counter += 1

        self.board = board

    def to_list(self):
        """Convert dictionary to list"""

        position_counter = 1
        board_list = []

        for row in range(NUM_ROWS):
            curr_row = []
            for col in range(NUM_COLS):
                curr_row.append(self.board[position_counter])
                position_counter += 1
            board_list.append(curr_row)

        return board_list

    def add_position(self, slot, mark):
        pass

    def draw(self):
        """ASCII representation of game"""

        # convert board dictionary to board list

        board_text = ""

        for row in self.to_list():
            row_text = (' | '.join([str(square) for square in row]))
            board_text += f' {row_text}'
            board_text += '\n'
            board_text += SEPARATOR

        # remove last line
        board_text = board_text[:-len(SEPARATOR)]

        return board_text

    def __repr__(self):
        return self.draw()


if __name__ == '__main__':
    new_game = Board()

    # Basic idea:
    #   1. Set it up so we can enter X and O into Board
    #   2. Check winning conditions
    #   3. Write tests
    #   4. Design AI
    #   5. Reach is creating neural network on Tic Tac Toe and try on Connect 4

    # Game Loop
    #   Create game, X's turn. O's turn, etc etc
