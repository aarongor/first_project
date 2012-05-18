from bottle import route, run

@route('/')
def index():
  return 'Hello world'

@route('/aaron')
def aaron():
  return '<h1>HELLO CAT</h1><img src="http://s3.amazonaws.com/i.jpg.to/t/271"/><em>I am cool</em>'

@route('/yefim')
def yefim():
  return 'hello yefim'

run(host='localhost', port=3000)

