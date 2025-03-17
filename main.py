import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))

from main import app
from fastapi.middleware.wsgi import WSGIMiddleware

application = WSGIMiddleware(app)
