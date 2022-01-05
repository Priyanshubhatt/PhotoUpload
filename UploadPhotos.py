import tornado.web
import tornado.ioloop

class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8080/img/{f.filename}")
    def get(self):
        self.render("index")


if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.instance().start()