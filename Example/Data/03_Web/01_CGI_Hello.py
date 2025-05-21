import http.server

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi_bin"]

port = 8080
server_address = ("", port)

httpd = server(server_address, handler)

httpd.serve_forever()