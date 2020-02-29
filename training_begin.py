import cv2
from paddles import detect_paddles
from define_traces import define_trace
from random import seed
from random import randint
def training_begin (cap, borders):
    seed(5)
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # odbicie lustrzane
    points = define_trace(borders)
    point1 = points.get()
    point2 = points.get()
    while (not points.empty()):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # odbicie lustrzane
        bin = detect_paddles(frame)
        if point_reched(point1,frame) and point_reched(point2,frame):
            point1 = points.get()
            point2 = points.get()
        frame = cv2.circle(frame, (point1[0], point1[1]), 2, (255, 0, 0), 10)
        frame = cv2.circle(frame, (point2[0], point2[1]), 2, (255, 0, 0), 10)
        cv2.imshow("img",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return randint(0,1000)

def point_reched(point,frame):
    bin = detect_paddles(frame)
    reached = False
    for x in range(-3,3):
        for y in range(-3,3):
            if bin[point[1]+x,point[0]+y] == 255:
                reached = True
    return reached
