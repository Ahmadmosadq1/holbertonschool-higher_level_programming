from http.server import BaseHTTPRequestHandler, HTTPServer
import json
"""making a subclass from a built class BaseHTTPRequestHandler
to use its attribuutes like "path" """ 


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """a class inherted from BaseHTTPRequestHandler"""
    def do_GET(self):

        """if the path url ends with / or empty, you can accept it"""
        """this is considered a defult home page for the websoite"""
        if self.path == "" or self.path =="/":
            self.send_response(200)

            """on the header of the request , before the body, we can put
            the below key and value"""
            self.send_header("Content-Type", "text/plain; charset=utf-8")

            """here, marks the end of the header of the request"""
            self.end_headers()

            """here, we can put the content of the body"""
            self.wfile.write(b"Hello, this is a simple API!")

            """if the url end point is /data"""
        elif self.path == "/data":
            json_dict = {"name": "John", "age": 30, "city": "New York"}
            content = json.dumps(json_dict).encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(content)


        elif self.path == "/status":
            """for status page"""
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", "0")
            self.end_headers()
            self.wfile.write("404 Not Found")
def running(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    this method runs the web server
    server class takes the url + the port as the first argument
    and handler class as a second argument
    """

    """# initialize the HTTP server instance"""
    server = server_class(("", port), handler_class)

    """# start handling requests in an infinite loop"""

    print(f"Listening on http://localhost:{port}/")

    server.serve_forever()

if __name__=="__main__":
    running()

