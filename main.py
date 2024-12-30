board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], #8 #0 BLACK 
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], #7 #1
         ['.', '.', '.', '.', '.', '.', '.', '.'], #6 #2 (2,1)
         ['.', '.', '.', '.', '.', '.', '.', '.'], #5 #3
         ['.', '.', '.', '.', '.', '.', '.', '.'], #4 #4
         ['.', '.', '.', '.', '.', '.', '.', '.'], #3 #5 (5, 4)
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], #2 #6
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']] #1 #7 WHITE
     #     a    b    c    d    e    f    g    h
     #     0    1    2    3    4    5    6    7


#lowercase characters are black
#uppercase characters are white

# TO DO:

# move pieces not working
#pawns

# Traceback (most recent call last):
#   File "/Users/nick/Desktop/VSCode/Python/Chess/main.py", line 565, in <module>
#     print(legal_move(BLACK, move))
#           ~~~~~~~~~~^^^^^^^^^^^^^
#   File "/Users/nick/Desktop/VSCode/Python/Chess/main.py", line 480, in legal_move
#     pieces = find_piece(board, move, player)
#   File "/Users/nick/Desktop/VSCode/Python/Chess/main.py", line 202, in find_piece
#     if board[row][column] == move[0].lower():
#                              ~~~~^^^
# TypeError: 'NoneType' object is not subscriptable

#
#work on black

# Add in support for less common moves
#Qh4xe1
#Qh4xe1#
#Qh4xe1+

# Add in support for promotion and castling and en passant
#e8Q - promotion
# 0-0 castling
# exd5 e.p  en passant 
#draw offer
#resign
#move database

# 2 player support for print_board()

# function for type of move                         x
# function for valid move                           x
# function for user input                           x
# function for moving pieces                        x
# function for checking if the move is valid        x
# function for checking if the move is legal        x
# function for checking if stalemate                
# function for checking if checkmate                
# function for checking if check                    
# function for printing the board                   x

# COLORS
WHITE = 0
BLACK = 1

# TYPES OF MOVES
NORMAL = 0
TAKE = 1
CHECK = 2
CHECKMATE = 3
SAME_FILE = 4
SAME_RANK = 5
TAKE_AND_CHECK = 6
TAKE_AND_CHECKMATE = 7
SAME_FILE_AND_CHECKMATE = 8

correct_turn_white = False
correct_turn_black = False
player = 0

move_database = []







def type_of_move(move):
    if len(move) == 3:
        return NORMAL
    elif len(move) == 4:
        if move[1] == "x":
            return TAKE
        elif move[3] == "+":
            return CHECK
        elif move[3] == "#":
            return CHECKMATE
        elif move[1] in "abcdefgh":
            return SAME_FILE
        elif move[1] in "12345678":
            return SAME_RANK
    elif len(move) == 5:
        if move[1] == "x" and move[4] == "+":
            return TAKE_AND_CHECK
        elif move[1] == "x" and move[4] == "#":
            return TAKE_AND_CHECKMATE
        elif move[1] in "abcdefgh" and move[4] == "#":
            return SAME_FILE_AND_CHECKMATE
        # in progress







def valid_move(move):
    if type_of_move(move) == NORMAL:
        if move[0] in 'RNBQKP':
            if move[1] in 'abcdefgh':
                if move[2] in '12345678':
                    return True
                else:
                    return False    
            else:
                return False
        else:
            return False
    elif type_of_move(move) == TAKE:
        if move[0] in 'RNBQKP':
            if move[1] == 'x':
                if move[2] in 'abcdefgh':
                    if move[3] in 'abcdefgh':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif type_of_move(move) == CHECK:
        if move[0] in 'RNBQKP':
            if move[1] in 'abcdefgh':
                if move[2] in '12345678':
                    if move[3] == '+':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif type_of_move(move) == CHECKMATE:
        if move[0] in 'RNBQKP':
            if move[1] in 'abcdefgh':
                if move[2] in '12345678':
                    if move[3] == '#':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif type_of_move(move) == SAME_FILE:
        if move[0] in 'RNBQKP':
            if move[1] in 'abcdefgh':
                if move[2] in 'abcdefgh':
                    if move[3] in '12345678':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif type_of_move(move) == SAME_RANK:
        if move[0] in 'RNBQKP':
            if move[1] in '12345678':
                if move[2] in 'abcdefgh':
                    if move[3] in '12345678':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False







def find_piece(board, move, player):
    possible_pieces = []
    for row in range(len(board)):
        for column in range(len(board[0])):
            if player == WHITE:
                if board[row][column] == move[0].upper():
                    possible_pieces.append((row, column))
                else:
                    continue
            if player == BLACK:
                if board[row][column] == move[0].lower():
                    possible_pieces.append((row, column))
                else:
                    continue
    return possible_pieces






def letter_to_num(move):
    if type_of_move(move) == NORMAL or type_of_move(move) == CHECK or type_of_move(move) == CHECKMATE:
        return ord(move[1]) - 97
    elif type_of_move(move) == TAKE or type_of_move(move) == SAME_FILE or type_of_move(move) == SAME_RANK:
        return ord(move[2]) - 97






def row_to_num(move):
    if type_of_move(move) == NORMAL or type_of_move(move) == SAME_FILE:
        return 8 - int(move[2])
    elif type_of_move(move) == TAKE or type_of_move(move) == CHECK or type_of_move(move) == CHECKMATE: # Bxf6 [3]
        return 8 - int(move[3])
    elif type_of_move(move) == SAME_RANK:
        return 8 - int(move[1])







def userinput_to_chessboard(move):
    return (row_to_num(move), letter_to_num(move))








def legal_move_notoccupied(player, move): #special case for pawns
    if type_of_move(move) == NORMAL:
        if player == WHITE:
            if board[row_to_num(move)][letter_to_num(move)] in "rnbqkp.":
                return True
            else:
                print("You can't attack your own piece.")
                return False
        if player == BLACK:
            if board[row_to_num(move)][letter_to_num(move)] in "RNBQKP.":
                return True
            else:
                print("You can't attack your own piece.")
                return False
    if type_of_move(move) == SAME_FILE:
        pass







def legal_move_trait(move, piece): #special case for pawns
    (old_row, old_column) = piece
    if type_of_move(move) == NORMAL:
        if move[0] == 'R':
            if old_row == row_to_num(move) or old_column == letter_to_num(move):
                return True
        elif move[0] == 'N':
            tuple1 = (old_row, old_column)
            tuple2 = userinput_to_chessboard(move)
            
            result_list = [x - y for x, y in zip(tuple1, tuple2)]
            result_tuple = tuple(result_list)                                                                           # first, second = result_tuple                    
            if result_tuple in [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:                 # if abs(first) == 1 or abs(first) == 2 ^ abs(second) == 1 or abs(second) == 2:           
                return True            
        elif move[0] == 'B':            
            if abs(old_row - row_to_num(move)) == abs(old_column - letter_to_num(move)):                
                return True             
        elif move[0] == 'Q':
            if old_row == row_to_num(move) or old_column == letter_to_num(move) or abs(old_row - row_to_num(move)) == abs(old_column - letter_to_num(move)):
                return True
        elif move[0] == 'K':
            if abs(old_row - row_to_num(move)) <= 1 and abs(old_column - letter_to_num(move)) <= 1:
                return True
        elif move[0] == 'P':
            if old_column == letter_to_num(move):
                if player == WHITE:
                    if old_row == 1:
                        if old_row - 2 == row_to_num(move) or old_row - 1 == row_to_num(move):
                            return True
                    else:
                        if old_row - 1 == row_to_num(move):
                            return True
                if player == BLACK:
                    if old_row == 6:
                        if old_row + 2 == row_to_num(move) or old_row + 1 == row_to_num(move):
                            return True
                    else:
                        if old_row + 1 == row_to_num(move):
                            return True
            return False


    elif type_of_move(move) == TAKE:
        pass
    elif type_of_move(move) == CHECK:
        pass
    elif type_of_move(move) == CHECKMATE:
        pass
    elif type_of_move(move) == SAME_FILE:
        pass
    elif type_of_move(move) == SAME_RANK:
        pass
    else:
        return False




    # pieces = find_piece(board, move, player)
    # for piece in pieces:                                 #      for i in range(len(find_piece(board, move))):
    #     (old_row, old_column) = piece                    #      (old_row, old_column) = find_piece(board, move)[i]



def legal_move_not_blocked(player, move, piece): #only for rooks, bishops, and queens and first pawn move
        (old_row, old_column) = piece
        if type_of_move(move) == NORMAL:


            if move[0] == 'R':
                if old_row == row_to_num(move):
                    for column in range(min(old_column, letter_to_num(move)), max(old_column, letter_to_num(move))):
                        if piece[1] == column or piece[1] == letter_to_num(move):
                            continue
                        if board[old_row][column] != ".":
                            print("Rooks can't jump")
                            return False
                    return True
                elif old_column == letter_to_num(move):
                    for row in range(min(old_row, row_to_num(move)), max(old_row, row_to_num(move))):
                        if piece[0] == row or row == row_to_num(move):
                            continue
                        if board[row][old_column] != ".":
                            print("Rooks can't jump")
                            return False
                    return True
                

            elif move[0] == 'B':
                if old_row < row_to_num(move) and old_column < letter_to_num(move): # down right
                    for row in range (old_row, row_to_num(move)):
                        for column in range(old_column, letter_to_num(move)):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                if old_row < row_to_num(move) and old_column > letter_to_num(move): # down left
                    for row in range (old_row, row_to_num(move)):
                        for column in range(letter_to_num(move), old_column):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                if old_row > row_to_num(move) and old_column < letter_to_num(move): # up right
                    for row in range (row_to_num(move), old_row):
                        for column in range(old_column, letter_to_num(move)):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                if old_row > row_to_num(move) and old_column > letter_to_num(move): # up left
                    for row in range (row_to_num(move), old_row):
                        for column in range(letter_to_num(move), old_column):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                

            elif move[0] == 'Q':
                if old_row == row_to_num(move):
                    for column in range(min(old_column, letter_to_num(move)), max(old_column, letter_to_num(move))):
                        if piece[1] == column or piece[1] == letter_to_num(move):
                            continue
                        if board[old_row][column] != ".":
                            print("Rooks can't jump")
                            return False
                    return True
                elif old_column == letter_to_num(move):
                    for row in range(min(old_row, row_to_num(move)), max(old_row, row_to_num(move))):
                        if piece[0] == row or row == row_to_num(move):
                            continue
                        if board[row][old_column] != ".":
                            print("Rooks can't jump")
                            return False
                    return True
                
                elif old_row < row_to_num(move) and old_column < letter_to_num(move): # down right
                    for row in range (old_row, row_to_num(move)):
                        for column in range(old_column, letter_to_num(move)):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                elif old_row < row_to_num(move) and old_column > letter_to_num(move): # down left
                    for row in range (old_row, row_to_num(move)):
                        for column in range(letter_to_num(move), old_column):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                elif old_row > row_to_num(move) and old_column < letter_to_num(move): # up right
                    for row in range (row_to_num(move), old_row):
                        for column in range(old_column, letter_to_num(move)):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                elif old_row > row_to_num(move) and old_column > letter_to_num(move): # up left
                    for row in range (row_to_num(move), old_row):
                        for column in range(letter_to_num(move), old_column):
                            if abs(old_row - row) == abs(old_column - column):
                                if row == old_row and column == old_column:
                                    continue
                                if board[row][column] != ".":
                                    print("Bishops can't jump")
                                    return False
                                else:
                                    continue
                            else:
                                continue
                    return True
                    
            if move[0] == 'P':
                if player == WHITE:
                    if board[old_row - 1][old_column] != ".":
                        return False
                    else:
                        return True
                elif player == BLACK:
                    if board[old_row + 1][old_column] != ".":
                        return False
                    else:
                        return True

            if move[0] == 'K':
                # if check_check() or check_checkmate():
                    # return False
                return True
            if move[0] == 'N':
                return True


            
        elif type_of_move(move) == TAKE:
            pass
        elif type_of_move(move) == CHECK:
            pass
        elif type_of_move(move) == CHECKMATE:
            pass
        elif type_of_move(move) == SAME_FILE:
            pass
        elif type_of_move(move) == SAME_RANK:
            pass










def legal_move(player, move):
    pieces = find_piece(board, move, player)
    for piece in pieces:
        if type_of_move(move) == NORMAL:
            if legal_move_notoccupied(player, move):
                if legal_move_trait(move, piece) and legal_move_not_blocked(player, move, piece):
                    move_piece(player, piece)
                    return True
#not occupied and trait are not working





def check_stalemate(player):
    pass
    #check how many possible moves for king
    #check how many of the other teams pieces (using an array) can attack 1 square from the king (row or column)
    #compare the two numbers to determine stalemate
    #check no other pieces can move (array of 0)





def check_checkmate(player):
    if check_check(player) and check_stalemate(player): # and no possible moves to get out of check!!!
        return True







def check_check(player):
    pass
    #check how many of the other teams pieces (using an array) can move to the same square as the king
    #if there is a piece that can attack the king, return True



def print_board(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            print(board[row][column], end='')
        print() # newline




def get_user_input(player):
    move = input(f"{player} write your move (Kf5): ")
    move = move.strip()
    move = list(move)
    if valid_move(move) and legal_move(player, move):
        return move
    else:
        print("Please enter a valid move. (Kf5)")
        get_user_input(player)









def move_piece(player, move):
    if type_of_move(move) == NORMAL:
        if player == WHITE:
            board[row_to_num(move)][letter_to_num(move)] = move[0]
            board[move[0]][move[1]] = "."
            move_database.append(move)
        if player == BLACK:
            board[row_to_num(move)][letter_to_num(move)] = move[0].tolower()
            board[move[0]][move[1]] = "."
            move_database.append(move)
    




player = WHITE

move = get_user_input(player)
print_board(board)
print(move_database)





# print_board(board)
# for row in range (3, 5):
#     for column in range(1, 4):
#         #if abs(old_row - row) == abs(old_column - column)
#          if abs(old_row - row) == abs(old_column - column):
#             board[row][column] = "0"

# print_board(board)




# tuple1 = (0, 6) (0,6)
# tuple2 = (2, 5) # (2, 5)

# result_list = [x - y for x, y in zip(tuple1, tuple2)]
# result_tuple = tuple(result_list)

# first, second = result_tuple

# if result_tuple in [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
# #if (abs(first) == 1 ^ abs(second) == 2) ^ (abs(first) == 2 or abs(second) == 1):
#     print(1)
# else:
#     print(0)