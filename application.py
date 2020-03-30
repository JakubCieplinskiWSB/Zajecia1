from flask import Flask, render_template, redirect, url_for
from forms import IndexForm
from MongoHandler import MongoHandler, formContent
from MailSender import MailSender
import feedparser
import thread

app = Flask(__name__)

sendGridAPI = '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'
app.config['SECRET_KEY'] = 'KEY'
uri = "mongodb://spite:pxbZMHQwC4PiWLwvvByneG1mvoyn4g2wOxsbkRSfgNl9rgGUOaxoJsjmyTOqKxJjCipPmVpNFqqCic2hokGIAA==@spite.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@spite@&retrywrites=false"
senderEmail = 'yourrssfeed@feed.com'

mongo = MongoHandler(uri)
mail = MailSender(sendGridAPI)

def parseAndSendEmail(url,email):
    content = ""
    title = "Your RSS Feed"
    for urls in url:
        newsFeed = feedparser.parse(urls)
        content += "<h1>"
        content += newsFeed.channel.title
        content += "</h1><br>"
        for entry in newsFeed.entries:
                content += "<a href=" + entry.link + ">"
                content += entry.summary
                content += "</a>"
                content += "<br><br>"
    mail.send(senderEmail, str(email), title, content)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    indexForm = IndexForm()
    if indexForm.save.data:
        if indexForm.rss.data:
            content = formContent.getDictionary(indexForm.email.data, indexForm.rss.data)
            mongo.insert(content)
            return redirect(url_for('index'))
    if indexForm.send.data:
        feeds = mongo.getFeedsForAddress(indexForm.email.data)
        try:
            thread.start_new_thread(parseAndSendEmail, (feeds, indexForm.email.data))
            print("Started thread")
        except:
            print("Error starting thread")
        print()
        return redirect(url_for('index'))
    return render_template("index.html", title="Index", form=indexForm)
    
if __name__ == '__main__':
        app.run(host='0.0.0.0')