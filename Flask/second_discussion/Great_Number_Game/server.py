import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'great_number_game_secret_key'

leaderboard = []

@app.route('/')
def index():
    if 'target' not in session:
        session['target'] = random.randint(1, 100)
    if 'attempts' not in session:
        session['attempts'] = 0
    if 'game_over' not in session:
        session['game_over'] = False
    return render_template('index.html', leaderboard=leaderboard)

@app.route('/guess', methods=['POST'])
def guess():
    if session.get('game_over'):
        return redirect('/')

    guess_val = int(request.form['guess'])
    session['attempts'] += 1

    if guess_val == session['target']:
        session['result'] = 'correct'
        session['game_over'] = True
    elif session['attempts'] >= 5:
        session['result'] = 'lose'
        session['game_over'] = True
    elif guess_val < session['target']:
        session['result'] = 'low'
    else:
        session['result'] = 'high'

    return redirect('/')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    name = request.form['name']
    leaderboard.append({'name': name, 'attempts': session.get('attempts', 0)})
    return redirect('/leaderboard')

@app.route('/leaderboard')
def show_leaderboard():
    return render_template('leaderboard.html', leaderboard=leaderboard)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)