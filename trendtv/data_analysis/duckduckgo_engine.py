import duckduckgo

def get_duckduckgo_content(term):
    response = duckduckgo.query(term)
    content = list()
    if response.type is "answer":
        for i in range(0,len(response.results)):
            content.append({"type":"url","data":{"url":response.results[i].url,"info":response.results[i].text},"score":3})
    return content

    

