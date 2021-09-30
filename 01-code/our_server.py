from flask import Flask, abort
from prometheus_flask_exporter import PrometheusMetrics
from random import randint

app = Flask(__name__)
PrometheusMetrics(app)

@app.route("/")
def hello_world():
    if randint(0, 1) == 0:
        return "<h1>Hello, World!</h1>"
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
