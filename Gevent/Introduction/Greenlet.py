import greenlet
import time


def sing():
    while True:
        print("sing a song")
        time.sleep(1)

        greenlet_dance.switch()


def dance():
    while True:
        print("dance on the floor")
        time.sleep(1)

        greenlet_sing.switch()



greenlet_sing = greenlet.greenlet(sing)
greenlet_dance = greenlet.greenlet(dance)

# 开启
greenlet_sing.switch()
