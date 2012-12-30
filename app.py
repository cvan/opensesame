import functools
import json
import os
import random

from flask import Flask, Response, request, render_template
from flask.views import MethodView

from common import redis

try:
    if os.environ.get('DEBUG'):
        import settings_local as settings
    else:
        import settings_prod as settings
except ImportError:
    import settings

app = Flask(__name__)


def jsonify(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        response = f(*args, **kw)
        return Response(json.dumps(response),
                        headers={'Content-Type': 'application/json'})
    return wrapper


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    debug = bool(os.environ.get('DEBUG'))
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug, host='0.0.0.0', port=port)
