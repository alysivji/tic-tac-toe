"""Tic-Tac-Toe Game"""

NUM_ROWS = 3
NUM_COLS = 3
SEPARATOR = '---|---|---\n'


class Board:
    """The board is made up of sqaures"""

    def __init__(self):
        """Set up board"""

        board = []

        for row in range(NUM_ROWS):
            row_to_add = []
            for col in range(NUM_COLS):
                row_to_add.append(' ')

            board.append(row_to_add)

        self.board = board

    def draw(self):
        """ASCII representation of game"""

        board_text = ""

        for row in self.board:
            row_text = (' | '.join([square if square is not None else ' '
                                    for square in row]))
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
