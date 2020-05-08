import os
from flask import Flask, request, render_template
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

app = Flask(__name__)

@app.route('/sendwa')
def sendwa():
    account_sid = request.args.get('account_sid')
    auth_token = request.args.get('auth_token')
    from_wa = request.args.get('from_wa')
    to_wa = request.args.get('to_wa')
    body_message = request.args.get('body_message')

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    account_sid = str(account_sid)
    auth_token = str(auth_token)
    from_wa = str(from_wa)
    to_wa = str(to_wa)
    body_message = str(body_message)

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(to="whatsapp:+{}".format(to_wa), from_="whatsapp:+{}".format(from_wa), body=body_message)

    return 'Sukses kirim via WA, pesan : {}'.format(body_message)
