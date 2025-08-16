class Board:
    def __init__(self, size):
        self.size = size
        self.players_moves = [[[0] * size for _ in range(size)] for _ in range(2)]
    
    def show(self):
        print("\n".join(["|".join(['X' if self.players_moves[0][i][j] else 'O' if self.players_moves[1][i][j] else ' ' for j in range(self.size)])  for i in range(self.size)]))

    def set_player_move(self, active_player, r,c):
        r,c = r-1, c-1
        if not self.is_valid_location(r,c):
            return 'invalid'
        self.players_moves[active_player -1][r][c] = 1
        status = self.check_player_win(active_player,r,c)
        if status == None:
            return 'valid'
        return status
        
    def is_valid_location(self, r,c):
        if 0 <= r < self.size and 0 <= c < self.size and not self.players_moves[0][r][c] and not self.players_moves[1][r][c]:
            return True
        return False

    def check_player_win(self,active_player,r,c):
        # check for row win
        if all([self.players_moves[active_player -1][r][j] for j in range(self.size)]):
            return 'win'
        #check for column win
        if all([self.players_moves[active_player -1][i][c] for i in range(self.size)]):
            return 'win'
        #check for main diagonal win if the move on the main diagonal
        if r == c and all([self.players_moves[active_player -1][i][j] for i in range(self.size) for j in range(self.size) if i == j]):
            return 'win'
        #check for reverse diagonal win if the move on the reverse diagonal
        if r + c == self.size -1 and all ([self.players_moves[active_player -1][i][j] for i in range(self.size) for j in range(self.size) if i +j == self.size -1]):
            return 'win'
        #check for tie
        if all([(self.players_moves[0][i][j] | self.players_moves[1][i][j]) for i in range(self.size) for j in range(self.size)]):
            return 'tie'
        return None

class GamePlay:
    def __init__(self):
        while True:
            board_size = input("Enter board size: ")
            if board_size.isdecimal():
                board_size = int(board_size)
                break
            else:
                print("Invalid board size! try again")
        self.board = Board(board_size)
        self.players_names = []
        self.players_names.append(input("Enter player one name: "))
        self.players_names.append(input("Enter player two name: "))
        self.active_player = 1
        self.play()

    def play(self):
        while True:
            self.board.show()
            while True:
                location = self.get_player_move()
                status = self.board.set_player_move(self.active_player, *location)
                if status == 'invalid':
                    print("Invalid location! try again")
                    continue
                break
            if status == 'win':
                self.board.show()
                print(f"Player {self.players_names[self.active_player -1]} wins!")
                return
            elif status == 'tie':
                self.board.show()
                print(f"Tie!")
                return
            self.active_player = -self.active_player +3  # f(1) = 2, f(2) = 1 => f(x) = -x + 3
            
    def get_player_move(self):
        while True:
            r,c = input(f"Player {self.players_names[self.active_player -1]}, make a move: ").split()
            if r.isdecimal() and c.isdecimal():
                r,c = int(r), int(c)
                break
            else:
                print("Invalid input must enter number values!")
        return r,c

GamePlay()