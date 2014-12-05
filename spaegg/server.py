from http.server import SimpleHTTPRequestHandler


class SpaeggHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        try:
            open(path, 'rb')
        except OSError:
            self.path = '/'
        return super(SpaeggHandler, self).send_head()
