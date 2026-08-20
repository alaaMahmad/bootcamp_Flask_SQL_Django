from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level_one():
    return render_template('index.html', times=3, color='lightblue')

@app.route('/play/<int:x>')
def level_two(x):
    return render_template('index.html', times=x, color='lightblue')

@app.route('/play/<int:x>/<color>')
def level_three(x, color):
    return render_template('index.html', times=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)