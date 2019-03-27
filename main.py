import tornado.ioloop
import tornado.web
import json

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

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} the course you are viewing is {courseId}")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("list.txt", "r")
        items = f.read().splitlines()
        f.close()
        self.write(json.dumps(items))

    def post(self):
        item = self.get_argument("item")
        f = open("list.txt", "a")
        f.write(f"{item}\n")
        f.close()
        self.write(json.dumps({"message": "Item added to file"}))

class jsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("js.html") 


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", indexMainHandler),
        (r"/isEven", queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        (r"/list", listRequestHandler),
        (r"/js", jsRequestHandler)
    ])

    port = 8888
    application.listen(port)
    print(f"Your application is listening at port{port}")
    tornado.ioloop.IOLoop.current().start()

    # investigate the difference between twisted and tornado and choose one
