import urllib
import urllib2
import simplejson as json

_TWITTER_TRENDS_URL = 'http://api.twitter.com/1/trends.json'

# Grab a trends json from the twitter api
def _get_trends_json():
    request = urllib2.Request(_TWITTER_TRENDS_URL)
    response = urllib2.urlopen(request)
    s = response.read();
    json_obj = json.loads(s)
    return json_obj

# Get a tuple (trends, as_of) where trends is a list of objects
# with members name, source, and url, and as_of is a string
# representing the date of these trends
def twitter_stream_get_trends():
    trends_json = _get_trends_json()
    trends = []
    for o in trends_json.get('trends'):
        t = { 
            "word": o.get('name'), 
            "source": 'twitter' 
        }
        trends.append(t)
    return trends
    
def _main():
    trends = twitter_stream_get_trends()     
    for t in trends:
        print t
    print ''

if __name__ == '__main__':
     exit(_main())
