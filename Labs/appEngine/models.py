from google.appengine.ext import ndb

class Meme(ndb.Model):
    url = ndb.StringProperty(required = True)
    top_text = ndb.StringProperty(required = True)
    bottom_text = ndb.StringProperty(required = True)
