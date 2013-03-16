from render import *
import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):	
    render(self,'front.html',{'mainpageTitle':'title','output':'sample output'})


app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
