from sendgrid import SendGridAPIClient, Content
from sendgrid.helpers.mail import Mail


class MailSender:
    def __init__(self, API_KEY):
        self.sg = SendGridAPIClient(API_KEY)
    
    def send(self, sender, receiver, subject, contentMessage):
        mail_txt = Content('text/html', contentMessage)
        message = Mail(
            from_email=sender,
            to_emails=receiver,
            subject=subject,
            html_content = mail_txt)
        response = self.sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)