from hand_data import get_hand_position
from lib import Leap
from db import add_data
from classifier import clf
import time

NUM_SAMPLES = 40
SAMPLE_DELAY = .3
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
        sample = get_hand_position(controller)
        while len(sample) != NUM_FEATURES:
            print "Please place only right hand in view"
            sample = get_hand_position(controller)
        print sample
        add_data(sign=training_char, **sample)
    print "Done training"


def guess_char():
    controller = Leap.Controller()
    print clf.predict([v for k, v in get_hand_position(controller=controller).iteritems()])


def train():
    while True:
        training_char = get_char_to_train()
        time.sleep(3)
        train_char(training_char)


def guess():
    while True:
        '''
        frame_chars = []
        for i in range(20):
            frame_chars.append(guess_char())

        # choose most common sample
        print max(set(frame_chars), key=frame_chars.count)
        '''
        guess_char()
        time.sleep(1)

if __name__ == "__main__":
    #train()
    guess()
