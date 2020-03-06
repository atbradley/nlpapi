from .newspaper.article import ArticleResource

def request_handler(event, context):
    url = event['queryStringParameters'].get('a', False)
        
    if not url:
        #TODO: Send an error message.
        return 
    
    ar = ArticleResource()
    return ar.article_response(url)