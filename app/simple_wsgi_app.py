import datetime
import json
from wsgiref.util import request_uri
def app(environ, start_response):

    #start_response('200 OK', [('Content-Type', 'application/json')])
    #test = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    #test1 = bytes (test,'utf-8') # or test.encode('utf-8')
    #return [test1]

    start_response('200 OK', [('Content-Type', 'text/html')])
    environ_dump = {}
    for i,k in environ.items():
        environ_dump[str(i)]=str(k)
    environ_dump = json.dumps(environ_dump)
    resp_str =  json.dumps( {'time': datetime.datetime.now().strftime('%H:%M:%S'), 'url':environ['HTTP_HOST']+environ['RAW_URI']} )
    return [bytes(resp_str, 'utf-8')]
    #return [bytes(environ_dump, 'utf-8')]
    #return [bytes(request_uri(environ)+'\n', 'utf-8')]


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
