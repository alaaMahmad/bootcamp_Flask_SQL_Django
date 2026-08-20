from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x=8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def rows_only(x):
    return render_template('index.html', x=x, y=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def rows_and_cols(x, y):
    return render_template('index.html', x=x, y=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def full_checkerboard(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)