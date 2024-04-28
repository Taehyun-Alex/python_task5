import signal
import sys


def sigint_handler(signal, frame):
    print("Received SIGINT signal -> Exiting")
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)
print("Program is running, press Control + C to exit.")

while True:
    pass
