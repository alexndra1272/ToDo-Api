from . import nota
from ..models import Nota
@nota.route('/')
def index():
    return 'Hello World!'

@nota.route('/nota')
def nota():
    return 'Hello Alex!'