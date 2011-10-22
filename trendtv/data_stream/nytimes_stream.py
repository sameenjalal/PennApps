import urllib
import urllib2
import simplejson as json

_ARTICLE_SEARCH_API_KEY = 'b2badc8ab3cd45c8a894d030c54ee38e:9:64861590'
_MOST_POPULAR_API_KEY = 'a7db1e6da44d7cacabdd0cd510c961a5:18:64861590'
_MAX_ARTICLES = 10

_NYTIMES_TRENDS_URL = 'http://api.nytimes.com/svc/mostpopular/v2/'
_NYTIMES_TRENDS_URL += 'mostviewed/all-sections/1?api-key='
_NYTIMES_TRENDS_URL += _MOST_POPULAR_API_KEY
_NYTIMES_TRENDS_URL += '&max=10'


# Grab a trends json from the twitter api
def _get_trends_json():
    request = urllib2.Request(_NYTIMES_TRENDS_URL)
    response = urllib2.urlopen(request)
    s = response.read();
    json_obj = json.loads(s)
    return json_obj

def nytimes_stream_get_trends():
    trends_json = _get_trends_json()
    trends = []
    n = 0
    for o in trends_json.get('results'):
        tag_list = []
        had_facet = 0
        if o.get('des_facet') != "":
            tag_list += o.get('des_facet')
            had_facet = True
        if o.get('org_facet') != "":
            tag_list += o.get('org_facet')
            had_facet = True
        if o.get('geo_facet') != "":
            tag_list += o.get('geo_facet')
            had_facet = True
        if o.get('per_facet') != "":
            tag_list += o.get('per_facet')
            had_facet = True
        if not had_facet:
            continue
        else:
            n += 1
        if n >= _MAX_ARTICLES:
            break
        for tag in tag_list:
            for w in tag.split(', '):
                t = { "word": w, "source": 'nytimes' }
                trends.append(t)
    return trends
    
def _main():
    trends = nytimes_stream_get_trends()
    print 'Hottest nytimes keywords:'
    for t in trends:
        print t
    print ''

if __name__ == '__main__':
     exit(_main())
