import tornado.web
import tornado.ioloop
import tornado.httpserver
import config
from application import Application


if __name__ == '__main__':
    app = Application()
    app.listen(config.options.get('port'))
    tornado.ioloop.IOLoop.current().start()
