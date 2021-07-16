from flask import Flask,jsonify
from Processor import Processor
from flask import request, render_template
import json

app = Flask(__name__)
obj1 = Processor()


@app.route('/recommend', methods=["POST"])
def recommend():

    name = request.form.get('name')
    print(obj1.predict(name))
    print(type(obj1.predict(name)))
    return render_template('response.html', data=jsonify(obj1.predict(name)))



@app.route('/')
def welcome():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
