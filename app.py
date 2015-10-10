from classifier import clf
from flask import Flask, render_template, jsonify
from hand_data import get_hand_position
from lib import Leap
import random

app = Flask(__name__)
controller = Leap.Controller()
controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
past_symbol = None

@app.route('/')
def hello():
    return render_template('ui.html')

@app.route('/current')
def current_symbol():
    global past_symbol

    hand_pos = get_hand_position(controller)
    if not hand_pos:
        new = past_symbol != ' '
        past_symbol = ' '
        return jsonify(symbol=' ', new=new)

    features = [v for k, v in hand_pos.iteritems()]
    symbol = ''.join(clf.predict(features))

    new = past_symbol != symbol
    past_symbol = symbol

    return jsonify(symbol=symbol, new=new)

if __name__ == '__main__':
    app.run(debug=True)
