from flask import Flask, render_template
from forms import IndexForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'

test = {"author": "Mike",
        "text": "My first blog post!"}





@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    indexForm = IndexForm()
    return render_template("index.html", title="Index", form=indexForm)
