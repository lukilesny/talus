import time
from threading import Timer
from capture_video import capture_video
def main():
    starttime = time.time()
    while(True):
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))
        capture_video()

if __name__ == "__main__":
    main()

