"""Tic-Tac-Toe Game"""

NUM_ROWS = 3
NUM_COLS = 3
SEPARATOR = '---|---|---\n'


def all_same(items):
    return all(x == items[0] for x in items)


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

    def add_position(self, slot, mark):
        if type(self.board[slot]) is int:
            self.board[slot] = mark
        else:
            print('Already full')

    def check_victory(self):
        """Maybe check victory or check if catz game
        Or check if we can continue, or have function to do something like this
        """
        pass

        # brute force it (maybe look at filter solution later)
        winning_combos = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]

        for winning_combo in winning_combos:
            items = []
            for square in winning_combo:
                items.append(self.board[square])

            if all_same(items):
                print(f'{items[0]} wins!')
                return True

        return False

    def is_full(self):
        return set(self.board.values()) == set(['X', 'O'])

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
    print(new_game)
    new_game.add_position(1, 'X')
    new_game.check_victory()

    # Basic idea:
    #   3. Write tests
    #   4. Design AI
    #   5. Reach is creating neural network on Tic Tac Toe and try on Connect 4

    # Game Loop
    #   Create game, X's turn. O's turn, etc etc
