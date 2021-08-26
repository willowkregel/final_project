

import wsgiref.simple_server
import urllib.parse
import sqlite3
##I forgot to insert this into Github a while ago, I've been working on the code daily-ish
connection = sqlite3.connect('players.db')
cursor = connection.cursor()
class Tictactoe:
    def draw_board(self, board, start_response):
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        the_board = ('   |   |\n') + (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '\n') + ('   |   |\n') + ('-----------\n') + ('   |   |\n') + (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '\n') + ('   |   |\n') + ('-----------\n') + ('   |   |\n') + (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '\n') + ('   |   |\n')
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
    def get_player_input(self, board, environ, start_response):
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
                board[a] = 'X'
                board[b] = 'O'
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
    def is_space_free(self, board, environ):
        parameters = urllib.parse.parse_qs(environ['QUERY_STRING'])
        a = parameters['player1'][0] if 'player1' in parameters else None
        b = parameters['player2'][0] if 'player2' in parameters else None
        return (board[a] == '', board[b] == '')
    def is_board_full(self, board, environ):
        for i in range(1, 10):
            if Tictactoe.is_space_free(self, board, environ):
                return False
            return True
class Play(Tictactoe):
    def lets_play(self, start_response, environ):
        board1 = [' '] * 10
        Tictactoe.intro(self, start_response)
        Tictactoe.draw_board(self, board1, start_response)
        Tictactoe.get_player_input(self, board1, environ, start_response)
        if Tictactoe.winner(self, board1, 'X'):
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            Tictactoe.draw_board(self, board1, start_response)
            congratulations = 'Hooray! Player 1 has won the game!'
            start_response('200 OK', headers)
            return[congratulations.encode()]
        elif Tictactoe.winner(self, board1, 'O'):
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            Tictactoe.draw_board(self, board1, start_response)
            congratulations = 'Hooray! Player 2 has won the game!'
            start_response('200 OK', headers)
            return[congratulations.encode()]
        else:
            if Tictactoe.is_board_full(self, board1, environ):
                Tictactoe.draw_board(self, board1, start_response)
                tie = 'The game is a tie!'
                return[tie.encode()]
httpd = wsgiref.simple_server.make_server('', 8000, Play.lets_play(connection))
httpd.serve_forever()
