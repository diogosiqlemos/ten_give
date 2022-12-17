def application(environ, start_response):
    status = '200 OK'
    html = "Hello, WSGI"
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    return [bytes(html, 'utf-8')]

