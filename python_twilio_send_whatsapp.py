import os
from flask import Flask, request
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

app = Flask(__name__)

@app.route('/r')
def hello_world():

    return 'Hurrrrrrrrrrraaa'

@app.route('/calculator')
def cuba():
    awal = request.args.get('awal')
    akhir = request.args.get('akhir')

    hasil = int(awal) + int(akhir)
    return str(hasil)

@app.route('/kirimwa')
def kirim_wa():
    account_sid = request.args.get('account_sid')
    auth_token = request.args.get('auth_token')
    from_wa = request.args.get('from_wa')
    to_wa = request.args.get('to_wa')
    body_message = request.args.get('body_message')

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # account_sid = 'AC394d58a2fc9ae8ca6fb7bc3bacc37cbe'
    # auth_token = '81b425ff12855a14cfb04ea98f662058'
    account_sid = str(account_sid)
    auth_token = str(auth_token)
    from_wa = str(from_wa)
    to_wa = str(to_wa)
    body_message = str(body_message)

    client = Client(account_sid, auth_token, http_client=proxy_client)

    # twilio api calls will now work from behind the proxy:
    # message = client.messages.create(to="whatsapp:+6285947593178", from_='whatsapp:+14155238886', body='Bahaya, suhu rumah kamu {} derajat'.format(131))
    message = client.messages.create(to="whatsapp:+{}".format(to_wa), from_="whatsapp:+{}".format(from_wa), body=body_message)

    return 'Sukses kirim via WA, pesan : {}'.format(body_message)

if __name__ == '__main__':
    kirim_wa()
