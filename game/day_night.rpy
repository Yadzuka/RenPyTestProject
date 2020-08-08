######################################################
###  I want to try some time changing system here  ###
######################################################

init python:
    class Time:
        __time_now = 0;

        def __init__(self, time):
            self.__time_now = time

        def goForward():
            __time_now += 1

            if __time_now == 5:
                __time_now = 0;

        def getTime(self):
            return self.__time_now
