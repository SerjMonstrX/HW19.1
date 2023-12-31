from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os

hostName = "localhost"
serverPort = 8080

# Читаем содержимое html, записываем в переменную html_content
current_directory = os.path.dirname(os.path.abspath(__file__))
html_filename = 'index.html'
html_file_path = os.path.join(current_directory, html_filename)
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()


class MyServer(BaseHTTPRequestHandler):
    """Класс для создания простого HTTP-сервера"""

    def __get_html_content(self):
        """Возвращает содержимое файла index.html"""
        return html_content

    def do_GET(self):
        """Обрабатывает GET-запросы, возвращает содержимое файла index.html"""
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")