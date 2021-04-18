from flask import Flask, request, jsonify, render_template, url_for, redirect
import model

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

# 'Female','Service','No','2','3','3.8'


@app.route('/predict_burnout/<string:g>/<string:s>/<string:w>/<int:d>/<int:r>/<float:m>')
def pred(g, s, w, d, r, m):
    return model.burn_out_pred(g, s, w, d, r, m), 201


if __name__ == "__main__":
    app.run()
