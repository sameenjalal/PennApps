import urlparse
import twitter
import oauth2 as oauth
import re
import urllib 


url_checker = dict()
def twitter_auth():
    consumer_key = 'IqsuEo5xfTdWwjD1GZNSA'
    consumer_secret = 'dtYmqEekw53kia3MJhvDagdByWGxuTiqJfcdGkXw8A'

    request_token_url = 'https://api.twitter.com/oauth/request_token'
    access_token_url = 'http://api.twitter.com/oauth/access_token'
    authorize_url = 'http://api.twitter.com/oauth/authorize'

    #consumer = oauth.Consumer(consumer_key, consumer_secret)
    #client = oauth.Client(consumer)
    #resp, content = client.request(request_token_url, "GET")
    #request_token = dict(urlparse.parse_qsl(content))

    #access_token_key = request_token['oauth_token']
    #access_token_secret = request_token['oauth_token_secret']

    api = twitter.Api(consumer_key,consumer_secret,'36001624-5JrcK4i6UO69IFY6vxZdRYxKBqjB42mwjhoSzzSP6','jgKWIncNLnzBvvhFeVTE0lkMGi1PH222YCEHSZHY')

    return api


def twitter_pull(api,word):
    results = api.GetSearch(word,None,None,100)
    tweets = list()
    for result in results:
        tweets.append(result)
    return tweets

def twitter_extract_urls(api,tweets):
    pattern=re.compile('([a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}/*\S*)?$')
    urls=list()
    for tweet in tweets:
        found_urls = pattern.findall(tweet.text)
        found_urls = map(lambda x: x.strip("?.()[]{}!@#$^&*;'.,"), found_urls)
        urls.append(found_urls)
    urls = filter(lambda x: x,urls)
    return urls

def url_follow(url):
    if url_checker.has_key(url):
        return url_checker.get(url)
    try:
        r1 = urllib.urlopen('http://'+url)
        url_checker.update({url:r1.geturl()})
        return r1.geturl()
    except:
        pass

def unique_urls(urls):
    new_urls=list()
    for url in urls:
        new_urls.append(url_follow(url[0]))
    new_urls=filter(None,new_urls)
    url_dictionary = [{ "url": url, "count": new_urls.count(url)} for url in set(new_urls)]
    return url_dictionary 

def compile_twitter_content(tweets,url_data):
    content = list()
    for x in range(0,2):
        tweet = tweets[x]
        content.append({'type':'tweet','data':tweet,'score':3})
    for url in url_data:
        content.append({'type':'url','data':url['url'],'score':url['count']})
    return content

def twitter_similar_terms(tweets):
    stop_words=["a","i","it","am","at","on","in","of","to","is","so","too","my","the","and","but","are","very","here","even","from","them","then","than","this","that","though"]
    whole_text=''
    for tweet in tweets:
        whole_text += (tweet.text)
    whole_text = whole_text.split()
    whole_text_list=list()
    for word in whole_text:
        if not word in stop_words:
            whole_text_list.append(word)
    whole_text_dictionary = [{"word": word, "count": whole_text_list.count(word)} for word in set(whole_text_list)]

def get_twitter_content(term):
    api = twitter_auth()
    tweets = twitter_pull(api, term)
    urls = twitter_extract_urls(api,tweets)
    url_data = unique_urls(urls)
    twitter_similar_terms(tweets)
    return compile_twitter_content(tweets,url_data)

