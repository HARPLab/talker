#! /usr/bin/env python

import roslib
roslib.load_manifest('talker')
import rospy
import actionlib
import os

from talker.msg import SayAction, SayResult, PlayAction, PlayResult

class SayServer(object):
    def __init__(self):
        self.say_server = actionlib.SimpleActionServer('say', SayAction, self.say, False)
        self.say_server.start()

    def say(self, goal):
        rospy.loginfo('saying "{0}"'.format(goal.text))
        result = os.system('espeak "{0}"'.format(goal.text))
        if result == 0:
            self.say_server.set_succeeded(SayResult(True))
        else:
            self.say_server.set_succeeded(SayResult(False))


class PlayServer(object):
    def __init__(self):
        self.play_server = actionlib.SimpleActionServer('play', PlayAction, self.play, False)
        self.play_server.start()

    def play(self, goal):
        rospy.loginfo('playing "{0}"'.format(goal.text))
        result = os.system('espeak "{0}"'.format(goal.text))
        if result == 0:
            self.play_server.set_succeeded(PlayResult(True))
        else:
            self.play_server.set_succeeded(PlayResult(False))

if __name__ == '__main__':
    rospy.init_node('talker')
    say_server = SayServer()
    play_server = PlayServer()
    rospy.spin()
        
