import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

def send_email(sender, receiver, msg):
    message = Mail(
        from_email='lihirwe6@gmail.com',             
        to_emails=receiver,
        subject='Bongalo Notification',
        html_content=msg)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def send_sms(receiver, msg):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ['FROM_NUMBER']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=msg,
            from_=from_number,
            to=receiver
        )

    print(message.sid)