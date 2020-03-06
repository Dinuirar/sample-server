from src import app


@app.route('/')
@app.route('/index')
def index():
    return "hello world!!!"

@app.route('/xyz')
def xyz():
    return "test"


