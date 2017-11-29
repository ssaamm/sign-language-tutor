# ASL Tutor

<img alt="ASL Tutor logo" width="400px" src="http://i.imgur.com/ZPg5guN.png">

A language learning tool for American Sign Language which uses skeletal tracking
data from a Leap Motion and machine learning to interpret signs.

Please watch the [video demo](https://www.samueltaylor.org/projects/asl-tutor.html)!

This project was made in under 24 hours for TAMUHack 2015. Thanks to the
organizers!

## Setup

- Clone this repository
- Install packages from `requirements.txt`
- Start Redis running on localhost at port 6379
- `python app.py`
  - This step may take a few seconds the first time because the classifier has
    to be trained on the data. After that first time, the classifier is
    serialized to disk and loaded much more quickly on subsequent restart.
- Open a browser to the URL outputted in the console
