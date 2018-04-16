#from flask import Flask
import plivo

#app = Flask(__name__)

#@app.route('/')
#def index():
#	return 'Index Page'

#@app.route('/sndmsg/<dstnumber>')
def main(dstnumber):
    client = plivo.RestClient(auth_id = 'MAMGI5OTMXZTI0MMVMOG', auth_token = 'ZThmMzRjN2I1Y2U0ZWY2MDRkOTUxNTMzZjYzMzlh')
    try:
        response = client.messages.create(
            src='11111111111',
            dst= dstnumber,
            text='Hello, from Flask!',
        )
        #return 'Message succesfully sent to this number: %s'%dstnumber
        print(response.__dict__)
    except plivo.exceptions.PlivoRestError as e:
        print(e)

if __name__ == '__main__':
    main(919106054324)