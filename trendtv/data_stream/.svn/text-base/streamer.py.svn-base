from youtube_stream import youtube_stream_get_trends
from twitter_stream import twitter_stream_get_trends
from nytimes_stream import nytimes_stream_get_trends
from time import sleep

from trendtv.settings import *


stopwords = open(PROJECT_PATH+'/data_stream/stopwords').read()

def valid_word(word):
    return word.lower() not in stopwords

class streamer:
    def _serve_packets(self):
        stream_get_fns = [
                twitter_stream_get_trends,
                nytimes_stream_get_trends,
                youtube_stream_get_trends]
        r = True
        while r:
            for fn in stream_get_fns:
                packets = fn()
                for p in packets:
                    if not valid_word(p.get('word')):
                        continue
                    r = self.serve_packet_callback(p)
                    if not r:
                        break;

    def __init__(self, serve_packet_callback):
        self.serve_packet_callback = serve_packet_callback
        self._serve_packets()

def _serve_cb(packet):
    print '%s: %s' % (packet.get('source'), packet.get('word'))
    return True
    
def _main():
    st = streamer(_serve_cb)
    while True:
        sleep(1)

if __name__ == '__main__':
     exit(_main())
