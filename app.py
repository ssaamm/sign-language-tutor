from classifier import clf
from flask import Flask, render_template, jsonify
from hand_data import get_hand_position
from lib import Leap
import pickle
import random

app = Flask(__name__)

controller = Leap.Controller()
controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)

past_symbol = 'a'
prev_prediction = None

@app.route('/translate')
def translate():
    return render_template('ui.html')

@app.route('/')
def tutorial():
    return render_template('tutorial.html')

@app.route('/current')
def current_symbol():
    global past_symbol
    global prev_prediction

    # Is there a hand?
    hand_pos = get_hand_position(controller)
    if not hand_pos:
        new = past_symbol != ' '
        past_symbol = ' '
        return jsonify(symbol=' ', new=new)
    features = [v for k, v in hand_pos.iteritems()]

    # Do we have a new symbol?
    prediction = ''.join(clf.predict(features))
    if prediction == prev_prediction:
        # We good fam
        return jsonify(new=False, symbol=prediction)
    else:
        prev_prediction = prediction
        return jsonify(new=True, symbol=prediction)

@app.route('/splash')
def splash():
    return render_template('splash.html')


@app.route('/scoreboard')
def scoreboard():
    return jsonify(user_score=100)

if __name__ == '__main__':
    app.run(debug=True)
