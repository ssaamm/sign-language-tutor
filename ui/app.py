from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('ui.html')

@app.route('/current')
def current_symbol():
    return jsonify(symbol=random.choice('abcdefghijklmnopqrstuvwxyz    '),
            new=bool(random.getrandbits(1)))

if __name__ == '__main__':
    app.run(debug=True)
