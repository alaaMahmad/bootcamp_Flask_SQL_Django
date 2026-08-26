from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'super_secret_counter_key'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    if 'counter' not in session:
        session['counter'] = 0
    
    session['visits'] += 1
    session['counter'] += 1

    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = -1
    return redirect('/')

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    increment_value = int(request.form['increment'])
    session['counter'] += (increment_value - 1)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)