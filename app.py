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

with open('wordLemPoS/markov.pkl', 'r') as f:
    markov = pickle.load(f)

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
    print prediction, prev_prediction
    if prediction == prev_prediction:
        # We good fam
        return jsonify(new=False, symbol=prediction)
    elif prev_prediction:
        # Markov that like Kevin Bacon
        clf_probs = zip(clf.classes_, clf.predict_proba(features)[0])
        max_prob = max(clf_probs, key=lambda t: t[1])[1]

        max_freq = markov[prev_prediction].most_common(1)[0][1]
        mkv_probs = dict([(sym, max(0, (0.3 - max_prob) * freq / max_freq))
                for sym, freq in markov[prev_prediction].iteritems()])

        max_prob = 0.0
        for sym, prob in clf_probs:
            overall_prob = mkv_probs[sym] + prob if sym in mkv_probs else prob
            if overall_prob > max_prob:
                max_prob = overall_prob
                prediction = sym

        prev_prediction = prediction
        return jsonify(symbol=prediction, new=True)
    else:
        prev_prediction = prediction
        return jsonify(new=True, symbol=prediction)

if __name__ == '__main__':
    app.run(debug=True)
