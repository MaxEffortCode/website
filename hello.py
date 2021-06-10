import click
from flask import Flask
from gevent.pywsgi import WSGIServer
from flask import render_template

app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def index():
    return "Im in the mainframe"

@app.route('/hello2/', methods=['GET'])
def hello2(name=None):
    return render_template('hello2.html', name=name)





@app.route('/index/')


@app.route('/static/')

@app.route('/generic/')
@app.route('/elements/')






#needs to be last file routed
@app.route('/hello/')
def hello(name=None):
    return render_template('hello.html', name=name)





if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")pip
    # Production
    http_server = WSGIServer(('', 5000), app)

    http_server.serve_forever()


