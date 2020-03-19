from flask import Flask, render_template
from forms import IndexForm
from MongoHandler import MongoHandler, formContent
from MailSender import MailSender

app = Flask(__name__)
sendGridAPI = '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'
app.config['SECRET_KEY'] = 'KEY'
uri = "mongodb://spite:pxbZMHQwC4PiWLwvvByneG1mvoyn4g2wOxsbkRSfgNl9rgGUOaxoJsjmyTOqKxJjCipPmVpNFqqCic2hokGIAA==@spite.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@spite@&retrywrites=false"


mongo = MongoHandler(uri)
mail = MailSender(sendGridAPI)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    indexForm = IndexForm()
    if indexForm.validate_on_submit():
        content = formContent.getDictionary(indexForm.email.data, indexForm.rss.data)
        mongo.insert(content)
        documents = mongo.getDocuments()
        for document in documents:
                mail.send('testywdupe@testy.com', content['email'], 'Twoja stara', content['rss'])
        return render_template("index.html", title="Index", form=indexForm)


    return render_template("index.html", title="Index", form=indexForm)

    

if __name__ == '__main__':
        app.run(host='0.0.0.0')