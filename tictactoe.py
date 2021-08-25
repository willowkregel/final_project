
# Tic Tac Toe 
# Converting to OOC
import wsgiref.simple_server

import random

print('''
GREETINGS, welcome to a friendly 1v1 tic tac toe game!
Feel free to have a friend with you to play this simple
game, since this is fun for anyone of any age! There is
really nothing to explain, I hope you enjoy!''')
def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Lets either player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the first player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the players wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Player 1 has beaten you! P1 wins!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Player 2's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Player 2 has beaten you! P2 wins!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
##START OF OOC TICTACTOE
##I didn't see your code + I can't check if this code is OK (it's probably not) because my computer is weird-- feel free to fix it and ask me about snippets of code
import wsgiref.simple_server
import urllib.parse
import sqlite3
##I forgot to insert this into Github a while ago, I've been working on the code daily-ish
connection = sqlite3.connect('players.db')
cursor = connection.cursor()
class Tictactoe:
    def __init__(self, board):
        self.board = board
    def draw_board(self, start_response):
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        the_board = ('   |   |\n') + (' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9] + '\n') + ('   |   |\n') + ('-----------\n') + ('   |   |\n') + (' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6] + '\n') + ('   |   |\n') + ('-----------\n') + ('   |   |\n') + (' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3] + '\n') + ('   |   |\n')
        start_response('200 OK', headers)
        return[the_board.encode()]
    def intro(self, start_response):
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        intro = '''GREETINGS, welcome to a friendly 1 versus 1 Tic-Tac-Toe game!
        Feel free to have a friend with you to play this simple game, since this is fun for anyone of any age!
        Heads up: player 1 is X, and player 2 is O. Moves are between 1 to 9. To make a move, insert your move into the URL! 
        Additionally, if 2 players make a winning move at the same time, there will be a tie!
        There is nothing else to explain, I hope you enjoy!
        '''
        start_response('200 OK', headers)
        return[intro.encode()]
    def get_player_input(self, environ, start_response):
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        path = environ['PATH_INFO']
        parameters = urllib.parse.parse_qs(environ['QUERY_STRING'])
        a = parameters['player1'][0] if 'player1' in parameters else None
        b = parameters['player2'][0] if 'player2' in parameters else None
        connection.execute('CREATE TABLE player_info (player_1, player_2)')
        if path == '/move' and a and b:
            start_response('200 OK', headers)
            check = cursor.execute('SELECT * FROM player_info WHERE player1 = ? AND player2 = ?', [a, b]).fetchall()
            if check:
                return['Sorry, a player has already chosen that spot.'.encode()]
            else:
                connection.execute('INSERT INTO player_info VALUES (?, ?)', [a, b])
                self.board[a] = 'X'
                self.board[b] = 'O'
                connection.commit()
                return (a, b)
        if path == '/restart' and a and b:
            start_response('200 OK', headers)
            connection.execute('DELETE FROM player_info WHERE player1 > ? AND player2 > ?', [1, 1])
            connection.commit()
            return['Game successfully restarted.'.encode()]
    def winner(self, bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))
    def get_board_copy(self):
        dupe_board = []
        for i in self.board:
            dupe_board.append(i)
        return dupe_board
    def is_space_free(self, environ):
        parameters = urllib.parse.parse_qs(environ['QUERY_STRING'])
        a = parameters['player1'][0] if 'player1' in parameters else None
        b = parameters['player2'][0] if 'player2' in parameters else None
        return (self.board[a] == '', self.board[b] == '')
    def is_board_full(self):
        for i in range(1, 10):
            if Tictactoe.is_space_free(self.board, i):
                return False
            return True

class Play(Tictactoe):
    def play(self, start_response):
        board = [' '] * 10
        Tictactoe.__init__(self, board)
        Tictactoe.intro()
        Tictactoe.draw_board()
        Tictactoe.get_player_input()
        if Tictactoe.winner(board, 'X'):
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            Tictactoe.draw_board()
            congratulations = 'Hooray! Player 1 has won the game!'
            start_response('200 OK', headers)
            return[congratulations.encode()]
        elif Tictactoe.winner(board, 'O'):
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            Tictactoe.draw_board()
            congratulations = 'Hooray! Player 2 has won the game!'
            start_response('200 OK', headers)
            return[congratulations.encode()]
        else:
            if Tictactoe.is_board_full():
                Tictactoe.draw_board()
                tie = 'The game is a tie!'
                return[tie.encode()]
httpd = wsgiref.simple_server.make_server('', 8000, Play.play)
httpd.serve_forever()
