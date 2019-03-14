import webapp2
import jinja2
import os
from google.appengine.api import urlfetch

# defining template directory....
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

# this class is basically for rendering the template


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        self.render("shopping_list.html")

    def post(self):
        excel = self.request.get('Excel')
        coding = self.request.get('Coding')
        if excel:
            self.redirect('/excel')
        if coding:
            self.redirect('/coding')


class ExcelHandler(Handler):
    def get(self):
        self.render("extra.html")

    def post(self):
        endexcel = self.request.get('EndExcel')
        if endexcel:
            self.redirect('/')


class CodingHandler(Handler):
    def get(self):
        self.render("extra2.html")

    def post(self):
        endcoding = self.request.get('EndCoding')
        if endcoding:
            self.redirect('/')


# mapping webpages/.......
app = webapp2.WSGIApplication([
    ('/', MainPage), ('/excel', ExcelHandler), ('/coding', CodingHandler),
], debug=True)


# self.redirect("/excel")
