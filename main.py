import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class indexMainHandler(tornado.web.RequestHandler):
    """ This Allows me to serve static sites back to the client """
    def get(self):
        self.render("index.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
    """ get a query string from a user request and interpret it """
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer")
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", indexMainHandler),
        (r"/isEven", queryParamRequestHandler)
    ])

    port = 8888
    application.listen(port)
    print(f"Your application is listening at port{port}")
    tornado.ioloop.IOLoop.current().start()
