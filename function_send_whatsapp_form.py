import os
from flask import Flask, request, render_template
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

app = Flask(__name__)

@app.route('/kirimwa', methods=["GET","POST"])
def kirimwa():
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    if request.method == 'POST':
        client = Client(request.form['account_sid'], request.form['auth_token'], http_client=proxy_client )
        message = client.messages.create(to="whatsapp:+{}".format(str(request.form['to_wa'])), from_="whatsapp:+{}".format(str(request.form['from_wa'])), body=str(request.form['body_message']) )
    return render_template("form_wa.html")
