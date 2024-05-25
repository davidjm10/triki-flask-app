from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial empty board
board = [' ' for _ in range(9)]

def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8)   # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'Draw'
    return None

@app.route('/')
def index():
    return render_template('index.html', board=board, winner=None)

@app.route('/play/<int:position>', methods=['POST'])
def play(position):
    global board
    player = request.form['player']
    if board[position] == ' ':
        board[position] = player
        winner = check_winner(board)
        if winner:
            return render_template('index.html', board=board, winner=winner)
        else:
            return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    global board
    board = [' ' for _ in range(9)]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
