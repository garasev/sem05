import flask
import pickle
import os
import pandas as pd

port = int(os.getenv("PORT", 8080))
app = flask.Flask(__name__, template_folder='./')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))



if __name__ == '__main__':
    app.run(host='192.168.1.1', port=port)