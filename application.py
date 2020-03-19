from flask import Flask, render_template, redirect, url_for
from forms import IndexForm
from MongoHandler import MongoHandler, formContent
from MailSender import MailSender
import feedparser

app = Flask(__name__)

sendGridAPI = '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'
app.config['SECRET_KEY'] = 'KEY'
uri = "mongodb://spite:pxbZMHQwC4PiWLwvvByneG1mvoyn4g2wOxsbkRSfgNl9rgGUOaxoJsjmyTOqKxJjCipPmVpNFqqCic2hokGIAA==@spite.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@spite@&retrywrites=false"
senderEmail = 'yourrssfeed@feed.com'

mongo = MongoHandler(uri)
mail = MailSender(sendGridAPI)


def parseAndSendEmail(url,email):
        newsFeed = feedparser.parse(url)
        #title = newsFeed.feed.author
        title = "Your RSS Feed"
        content = ""
        for entry in newsFeed.entries:
                content += entry.summary
                content += "<br><br>"
        mail.send(senderEmail, str(email), title, content)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    indexForm = IndexForm()
    if indexForm.validate_on_submit():
            if indexForm.save.data:
                    if indexForm.rss.data:
                        content = formContent.getDictionary(indexForm.email.data, indexForm.rss.data)
                        mongo.insert(content)
                        return redirect(url_for('index'))
            if indexForm.send.data:
                feeds = mongo.getFeedsForAddress(indexForm.email.data)
                for feed in feeds:
                    parseAndSendEmail(feed, indexForm.email.data)
                return redirect(url_for('index'))
                
                

    return render_template("index.html", title="Index", form=indexForm)

    

if __name__ == '__main__':
        app.run(host='0.0.0.0')