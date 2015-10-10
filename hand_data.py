import time
from lib import Leap
from lib.Leap import Bone

'''
gets the current frame from controller
for each finger, stores the topmost end of each bone (4 points)
adjusts bone location relativity by subtracting the center of the palm
returns the adjusted bone locations in the form:
[(finger1bone1x, finger1bone1y, finger1bone1z), ... finger5bone4z)]
'''
def get_hand_position(controller):
    print "NEW FRAME"
    fingers = controller.frame().fingers
    finger_bones = []
    for finger in fingers:
        finger_bones.append(finger.bone(Bone.TYPE_METACARPAL).next_joint)
        finger_bones.append(finger.bone(Bone.TYPE_PROXIMAL).next_joint)
        finger_bones.append(finger.bone(Bone.TYPE_INTERMEDIATE).next_joint)
        finger_bones.append(finger.bone(Bone.TYPE_DISTAL).next_joint)

    # possible issue when more than one hand
    hands = controller.frame().hands
    hand_center = 0
    for hand in hands:
        hand_center = hand.palm_position

    calibrated_finger_bones = []
    for joint in finger_bones:
        calibrated_finger_bones.append(joint - hand_center)

    return calibrated_finger_bones


if __name__ == "__main__":

    controller = Leap.Controller()

    while True:
        get_hand_position(controller)
        time.sleep(1)
