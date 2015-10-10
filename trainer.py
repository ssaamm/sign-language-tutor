from hand_data import get_hand_position
from lib import Leap
from db import add_data
from classifier import clf
import time

NUM_SAMPLES = 100
SAMPLE_DELAY = .1
NUM_FEATURES = 60


def get_char_to_train():
    training_char = raw_input("Enter char to train: ")

    while len(training_char) != 1 or not training_char.isalpha():
        print "Please enter a single alpha character"
        training_char = raw_input("Enter char to train: ")

    return training_char.lower()


def train_char(training_char):
    controller = Leap.Controller()
    for t in range(NUM_SAMPLES):
        time.sleep(SAMPLE_DELAY)
        sample = get_hand_position(controller, True)
        while len(sample) != NUM_FEATURES:
            print "Please place only right hand in view"
            sample = get_hand_position(controller, True)
        print sample
        add_data(sign=training_char, **sample)
    print "Done training"


def guess_char():
    controller = Leap.Controller()
    frame_guesses = []
    for i in range(10):
        frame_guesses.append(clf.predict([v for k, v in get_hand_position(controller, True).iteritems()])[0])
    print max(set(frame_guesses), key=frame_guesses.count)


def train():
    while True:
        training_char = get_char_to_train()
        time.sleep(2)
        train_char(training_char)


def guess():
    while True:
        guess_char()
        time.sleep(1)

if __name__ == "__main__":
    #train()
    guess()
