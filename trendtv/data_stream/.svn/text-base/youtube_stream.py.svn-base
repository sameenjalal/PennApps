import urllib
import urllib2
import simplejson as json

_YOUTUBE_TRENDS_URL = """
https://gdata.youtube.com/feeds/api/standardfeeds/on_the_web/?alt=json&prettyprint=false&max-results=10
"""
_YOUTUBE_MAX_HITS = 10

# Grab a trends json from the youtube api
def _get_trends_json():
    request = urllib2.Request(_YOUTUBE_TRENDS_URL)
    response = urllib2.urlopen(request)
    s = response.read();
    json_obj = json.loads(s)
    return json_obj

# Get a list of rtd-packets that are hot on this stream
def youtube_stream_get_trends():
    trends_json = _get_trends_json()
    trends = []
    n = 0
    for o in trends_json.get('feed').get('entry'):
        words = o.get('media$group').get('media$keywords').get('$t')
        for w in words.split(','):
            t = {
                "word": w.strip(),
                "source": 'youtube'
            }
            trends.append(t)
        if n >= _YOUTUBE_MAX_HITS:
            break
        else:
            n += 1
    return trends
    
def _main():
    trends = youtube_stream_get_trends()     
    for t in trends:
        print t
    print ''

if __name__ == '__main__':
     exit(_main())
