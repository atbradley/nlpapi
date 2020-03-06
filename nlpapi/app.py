from .newspaper.article import ArticleResource

import falcon

from dotenv import load_dotenv
load_dotenv()

api = application = falcon.API()

api.add_route('/nlp/article', ArticleResource())