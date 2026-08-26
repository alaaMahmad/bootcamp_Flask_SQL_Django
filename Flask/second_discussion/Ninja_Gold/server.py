import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ninja_gold_secret_key'

BUILDINGS = {
    'farm': (10, 20),
    'cave': (5, 10),
    'house': (2, 5),
    'casino': (-50, 50)
}

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'moves' not in session:
        session['moves'] = 0
    if 'game_over' not in session:
        session['game_over'] = False
    if 'win_status' not in session:
        session['win_status'] = None

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']

    if building == 'reset':
        session.clear()
        return redirect('/')

    if session.get('game_over') or building not in BUILDINGS:
        return redirect('/')

    min_gold, max_gold = BUILDINGS[building]
    earned = random.randint(min_gold, max_gold)
    
    session['gold'] += earned
    session['moves'] += 1

    if earned >= 0:
        msg = f"Earned {earned} golds from the {building}!"
        color = 'green'
    else:
        msg = f"Entered a casino and lost {earned}"
        color = 'red'

    session['activities'].insert(0, {'msg': msg, 'color': color})

    if session['gold'] >= 250 and session['moves'] <= 15:
        session['game_over'] = True
        session['win_status'] = 'win'
    elif session['moves'] >= 15:
        session['game_over'] = True
        session['win_status'] = 'lose'

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)