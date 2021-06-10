import click
from flask import Flask
from gevent.pywsgi import WSGIServer
from flask import render_template

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return "Im in the mainframe"


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/index/')
@app.route('/index/*')

def hello(name=None):
    return render_template('hello.html', name=name)




if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")pip
    # Production
    http_server = WSGIServer(('', 5000), app)
    hello()

    http_server.serve_forever()


