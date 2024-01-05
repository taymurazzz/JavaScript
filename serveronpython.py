from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Открываем и читаем содержимое файла index.html
            with open('index.html', 'rb') as file:
                content = file.read()
            
            # Отправка заголовка ответа
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Отправка содержимого ответа
            self.wfile.write(content)

        except FileNotFoundError:
            # Если файл не найден, отправляем ошибку 404
            self.send_error(404, 'File Not Found')

if __name__ == '__main__':
    # Запуск сервера на порту 8000
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()
