import json
from pprint import pprint
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <title>Web Therapist</title>
    <meta charset=utf-8>

    <body>
      <h1>Personal Online Therapist</h1>
      <p>Type here:</br>
        <form action="." id="textform" method="POST">
          <textarea name="text"></textarea>
          <input type="submit" value="submit">
        </form>
      </p>
    </body>
           """

@app.route('/', methods=['POST'])
def check_textarea():
    text = request.form['text']
    processed_text = text.lower()

    with open('afinn.json') as data_file:
        data = json.load(data_file)
        text = request.form['text']
    for line in data:
            return (line)



if __name__ == "__main__":
    app.run(debug=True)
