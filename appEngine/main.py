import webapp2
import jinja2
import os
from models import Meme
from google.appengine.api import urlfetch
import json
#This initializes the jinja Environment
#SAME FOR EVERY app
#jinja2.Environment is a construction
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)
#Handler Sections
class MainPage(webapp2.RequestHandler):
    def get(self):
        api_url = "https://api.imgflip.com/get_memes"
        imgflip_response_json = urlfetch.fetch(api_url).content
        imgflip_response_raw = json.loads(imgflip_response_json)
        memeTemplates = []
        for meme in imgflip_response_raw['data']['memes']:
            memeTemplates.append(meme['url'])
        meme_dictionary = {
            "imgs" : memeTemplates
        }
        # self.response.headers["Content-Type"] = 'text/html'
        # self.response.write("<h1>How are you?</h1><h4>I'm doing fine</h4>")
        welcome_template = jinja_env.get_template('welcome.html')
        self.response.write(welcome_template.render(meme_dictionary))

class ResultPage(webapp2.RequestHandler):
    # def get(self):
    #     # self.response.headers["Content-Type"] = 'text/plain'
    #     # self.response.write("My name is Ryan")
    # result_template = jinja_env.get_template('result.html')
    # self.response.write(result_template.render())

    def post(self):
        top_line = self.request.get("top-line")
        bottom_line = self.request.get("bottom-line")
        meme_url = self.request.get("template")
        newMeme = Meme(url = meme_url, top_text = top_line,bottom_text = bottom_line)
        newMeme.put()
        results = {
            "top" : top_line,
            "bottom" : bottom_line,
            "url" : meme_url
        }
        result_template = jinja_env.get_template('result.html')
        self.response.write(result_template.render(results))
        print(top_line)

class Gallery(webapp2.RequestHandler):
    def get(self):
        memeStore = Meme.query().fetch()

        references = {
            "head1" : "Gallery",
            "memes" : memeStore

        }
        # self.response.headers["Content-Type"] = 'text/plain'
        # self.response.write("Here are some of my pictures: ")
        gallery_template = jinja_env.get_template('gallery.html')
        self.response.write(gallery_template.render(references))

class FAQ(webapp2.RequestHandler):
    def get(self):
        references = {
            "head1" : "Frequently Asked Questions"
        }
        # self.response.headers["Content-Type"] = 'text/plain'
        # self.response.write("Frequently Asked Questions")
        faq_template = jinja_env.get_template('faq.html')
        self.response.write(faq_template.render(references))



app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/result', ResultPage),
        ('/gallery', Gallery),
        ('/faq', FAQ)
    ],
    debug = True
)
