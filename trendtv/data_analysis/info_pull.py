import twitter_engine
import duckduckgo_engine

def get_content(term):
    content = list()
    content += twitter_engine.get_twitter_content(term)
    content += duckduckgo_engine.get_duckduckgo_content(term)
    return content
