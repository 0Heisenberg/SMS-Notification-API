# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return 'Index Page'

@app.route('/send_sms/')
def outbound_sms():

	auth_id = 'AUTH_ID_HERE'
	auth_token = 'AUTH_TOKEN_HERE'
	#from_number= request.form.get("fromnumber")
	#to_number= request.form.get("tonumber")
	#content= request.form.get("text")
	# import pdb;pdb.set_trace()

	client = plivo.RestClient(auth_id = 'AUTH_ID_HERE', auth_token = 'AUTH_TOKEN_HERE')

	try:
		response = client.messages.create(
			src = 'SRC_NUM', # Sender's phone number with country code
	    	dst = 'DST_NUM', # Receiver's phone Number with country code
	    	text = 'Enter your message here..',
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
