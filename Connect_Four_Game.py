NUMBER_OF_ROWS = 5
NUMBER_OF_COLUMNS = 5
COLUMN_WIDTH = 3
ROW_WIDTH = 1
DEFALUT_BOARD_SIGN = " "
SIGN1 = "+"
SIGN2 = "-"
SIGN3 = "|"
PLAYER1 = "X"
PLAYER2 = "O"
MOVES = ["X", "O"]
LEFT_SPACING = 5

class ConnectFour():

    def __init__(self):
        self.board = [[DEFALUT_BOARD_SIGN] * NUMBER_OF_COLUMNS for _ in range(NUMBER_OF_ROWS)]
        self.players = [PLAYER1, PLAYER2]

    def print_board(self):
        """Print the board according to the current board's condition."""
        print() # Clear one line

        def print_row_boudary():
            print(" "*LEFT_SPACING+SIGN1, end="")
            for _ in range(NUMBER_OF_COLUMNS):
                print(SIGN2*COLUMN_WIDTH , end=SIGN1)
            print()

        def print_row(row_number: int):
            for i in range(ROW_WIDTH):
                is_middle = (i == ROW_WIDTH//2)
                if is_middle: print(f"{row_number+1:^{LEFT_SPACING}}"+SIGN3, end="")
                else: print(" "*(LEFT_SPACING)+SIGN3, end="")
                for j in range(NUMBER_OF_COLUMNS):
                    if is_middle: print(" "*(left_space:=((COLUMN_WIDTH-1)//2)) + self.board[row_number][j] + " "*(COLUMN_WIDTH-left_space-1), end=SIGN3)   # We will print the element in the middle of the row
                    else: print(" "*COLUMN_WIDTH, end=SIGN3)
                print()
        
        # Print the header row of the column numbers
        print(" "*(LEFT_SPACING+1), end="")
        for i in range(1, NUMBER_OF_COLUMNS+1):
            print(f"{i:^{COLUMN_WIDTH}}", end=" ")
        print(" ")

        # Print the Row Boundary
        for row in range(NUMBER_OF_ROWS):
            print_row_boudary()
            print_row(row)
        print_row_boudary() # Print the last boundary which didn't print in the loop.

    def is_already_played(self, row_number: int, column_number:int):
        """Return True if the given position in the board is X, else return False."""
        return self.board[row_number-1][column_number-1] != DEFALUT_BOARD_SIGN
    
    def validate_position(self, row_number: int, column_number: int):
        """Return True if given row number is within the total rows and column number is within the total columns."""
        return 1 <= row_number <= NUMBER_OF_ROWS and 1 <= column_number <= NUMBER_OF_COLUMNS 

    def play_move(self, row_number: int, column_number: int, player: int):
        """Plays the move on the board, after validating the move."""
        self.board[row_number-1][column_number-1] = player

    def check_direction(self, row, col, player, direction, count=0):
        """Using recursion checks over every direction for the continuous 4 pattern of the player."""
        if not self.validate_position(row, col) or self.board[row-1][col-1] != player:
            return False

        count += 1
        if count == 4:
            return True

        # Move in the given direction
        row_offset, col_offset = direction
        return self.check_direction(row + row_offset, col + col_offset, player, direction, count)

    def check_winner(self, row, col, player):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # 8 directions
        for direction in directions:
            if self.check_direction(row, col, player, direction, 0):
                return True
        return False
    
    def select_names(self):
        player1 = input("\nEnter Player X's name: ")
        if not player1: 
            print("Cannot be blank.")
            return False
        player2 = input("Enter Player O's name: ")
        if not player2: 
            print("Cannot be blank.")
            return False
        self.players[0] = player1
        self.players[1] = player2
        return True
    
    def select_signs(self):
        player1_sign = input(f"Enter {self.players[0]}'s sign : ")
        if not player1_sign: 
            print("Cannot be Blank.")
            return False
        player2_sign = input(f"Enter {self.players[1]}'s Sign : ")
        if not player2_sign or player2_sign == player1_sign: 
            print("Cannot be Blank.")
            return False
        MOVES[0] = player1_sign
        MOVES[1] = player2_sign
        return True

    def play(self):

        print("\nWELCOME TO THE CONNECT FOUR 😎 GAME.")

        current_index = 0

        # Let the players select their names if they want
        
        while True:
            select_names = input("\nDo you want to Select Player names: ").lower()
            if select_names == "yes":
                if not self.select_names(): continue
                else:
                    print(f"\n🤝 {self.players[0].capitalize()} 🆚 {self.players[1].capitalize()}\n")
            else:
                print(f"\n🤝 Let's Gooo.....\n")

            break

        # Let the players select their own signs for the board
        while True:
            select_signs = input("\nDo you want to Select Your own signs instead of X and O? : ").lower()
            if select_signs == "yes":
                if not self.select_signs(): continue
                else:
                    print(f"\n🤝 Let's Gooo......\n\nPLAYER {self.players[0] if self.players != "X" else "1"} : {MOVES[0]} \nPLAYER {self.players[1] if self.players[1] != "O" else "2"} : {MOVES[1]}\n")

            print("\nLet's start the Game ⚔️ ⚔️ ⚔️.")
            break
                
        # Start the Game
        self.print_board()


        while True:
            current_player = self.players[current_index]
            move = MOVES[current_index]

            print(f"\n👉 It's {current_player}'s Turn\n")

            try:
                row = int(input("Row number: "))
                column = int(input("Column number: "))
            except ValueError as e:
                print("\n😵 Invalid Choice: Please Enter Integer.")
                continue
            else:
                if not self.validate_position(row, column): 
                    print("\n😵 Invalid Choice: Out of bounds.")
                    continue
                if self.is_already_played(row, column):
                    print("\n😵 Invalid Choice: Box already played.")
                    continue
                self.play_move(row, column, move)


            if self.check_winner(row, column, move):
                self.print_board()
                print("\n\nGAME OVER..🙋")
                print(f"{current_player} Player WON.....😁")
                break
            
            current_index = abs(current_index-1)

            self.print_board()

connectfourgame = ConnectFour()
connectfourgame.play()
