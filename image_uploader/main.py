import tornado.web # read docs
import tornado.ioloop # read docs

class uploadRoute(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]

        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8080/img/{f.filename}")

if (__name__ == '__main__'):

    # define the tornado app, this takes an array of handles as sets
    app = tornado.web.Application([
        # each set takes a route and a class for instruction
        ("/", uploadRoute),
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path":"img"})
    ])

# set the port for app to listen
port = 8080
app.listen(port)
print("listening on port {}".format(port))

# start the application loop # learn more
tornado.ioloop.IOLoop.instance().start()
