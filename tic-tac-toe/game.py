from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #to create a board
        self.current_winner = None #Keep track of winner

    def print_board(self):
        # for creating boxes for the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        # assigning numbers to the box in the board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # returns a list of available moves
        moves = []
        for (i,spot) in enumerate(self.board):
            # ['x','x','o'] => [(0,'x'),(1,'x'),(2,'o')]
            if spot == ' ':
                moves.append(i)
        return moves

        # this whole loop can be written as
        #  return [i for i,spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        # return len(self.available_moves())
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move and return true
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # checking the row
        row_index = square // 3
        row = self.board[row_index*3 :  (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # checking column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # checking diagonal
        # checking even positions can give you diagonal testing
        if square % 2 == 0:
            diagona1 = [self.board[i] for i in [0,4,8]] #left to right
            if all([spot == letter for spot in diagona1]):
                return True
            diagona2 = [self.board[i] for i in [0,4,8]] #right to left
            if all([spot == letter for spot in diagona2]):
                return True

        # if all these fails
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()

    letter = 'X'

    # iterating till all the empty squares are filled or u get 3 in row

    while game.empty_squares():
        # getting moves from appropriate players
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                print(letter + ' Wins !!!')
                return letter

            # For alternating the turns
            letter = 'O' if letter == 'X' else 'X'

            # Alternate way of writing above line
        # if letter == 'X':
        #     letter = 'O'
        # else:
        #     letter='X'


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)