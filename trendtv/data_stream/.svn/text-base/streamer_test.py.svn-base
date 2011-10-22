from time import sleep
from streamer import streamer

def _packet_callback(p):
    print '%s -> %s' % (p.get('source'), p.get('word'))
    return True

stream = streamer(_packet_callback)
while True:
    sleep(1)
