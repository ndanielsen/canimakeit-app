from flask import Flask, request, render_template
from model import info_to_making_it
import json

app = Flask('canimakeit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return app.send_static_file(path)


@app.route('/api/user-info', methods=['POST'])
def post():
    print '\nReceived: ', request.data, '\n\n'
    data = request.data
    making_it_by_state = info_to_making_it(data)
    return json.dumps(making_it_by_state)

if __name__ == '__main__':
    app.run()
