from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_users():
    users = [
        {'first_name': 'Alaa', 'last_name': 'Ahmad'},
        {'first_name': 'Bara', 'last_name': 'Salah'},
        {'first_name': 'Michael', 'last_name': 'Marajda'},
        {'first_name': 'Maryan', 'last_name': 'Qassis'}
    ]
    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)