from flask import Flask

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':

        #data = request.json
        #from_ = unquote(data.get('From'))
        #to = unquote(data.get('To'))
        #message = unquote(data.get('Body'))
        #date = unquote(data.get('Date'))
        #message_id = unquote(data.get('MessageSID'))

        # Process the data here
        #log = getMessageLog(from_, to)
        #responses = getResponse(message, log)
        sleep(1)
        return jsonify({'message': "webhook received"}), 200
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415
