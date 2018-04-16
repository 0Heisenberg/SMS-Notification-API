# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return 'Index Page'

@app.route('/send_sms/')
def outbound_sms():

	auth_id = 'MAMGI5OTMXZTI0MMVMOG'
	auth_token = 'ZThmMzRjN2I1Y2U0ZWY2MDRkOTUxNTMzZjYzMzlh'
	#from_number= request.form.get("fromnumber")
	#to_number= request.form.get("tonumber")
	#content= request.form.get("text")
	# import pdb;pdb.set_trace()

	client = plivo.RestClient(auth_id = 'MAMGI5OTMXZTI0MMVMOG', auth_token = 'ZThmMzRjN2I1Y2U0ZWY2MDRkOTUxNTMzZjYzMzlh')

	try:
		response = client.messages.create(
			src = '1234567', # Sender's phone number with country code
	    	dst = '919106054324', # Receiver's phone Number with country code
	    	text = 'You recived a call at +14153014707',
		)
	#response = p.send_message(params)
	# Prints the complete response
		return str(response)
	except plivo.exceptions.PlivoRestError as e:
		print(e)


#@app.route('/send_message/', methods=['GET'])    
#def outbound_sms_template():
	#return render_template('test_sms_flask.html')

if __name__ == "__main__":
    app.run(debug=True)
