from flask import *
import requests
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('layout.html')
@app.route("/todo")

def todo():

    return render_template('todo.html')


if __name__ == "__main__":
    app.run(debug=True)