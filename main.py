from flask import Flask, request, make_response
from firebase_admin import credentials, messaging
import firebase_admin
import os

import logging

cred = credentials.Certificate('secure/private-api-key.json')
firebase_admin.initialize_app(credential=cred)

# We want to clear out the logs
os.remove("logs/log.txt")

logging.basicConfig(filename="logs/log.txt", level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")

logging.debug("App is starting")

app = Flask(__name__)

def send_notification(content: object, is_data: bool):
    topic = content.get("topic")
    inner_data_object = content.get("data")

    try:
        #TODO: Add validations
        logging.debug(topic)
        logging.debug(inner_data_object)

        logging.debug("Send notification")
        if is_data:
            msg = messaging.Message(data=inner_data_object, topic=topic)
        else:
            msg = messaging.Message(notification=inner_data_object, topic=topic)
    
        messaging.send(msg)

        return True
    except Exception as e:
        logging.exception(e)
        return False

@app.route("/data", methods=['POST'])
def data():
    try:
        content = request.get_json()
        logging.debug(content)
        success = send_notification(content, True)
    
        if success == False:
            raise Exception("Issue creating message")
        return "Ok"
    
    except Exception as e:
        res = make_response("Bad request", 400)
        logging.exception(e)
        return res

@app.route("/notification", methods=['POST'])
def notification():
    try:
        content = request.get_json()
        logging.debug(content)
        success = send_notification(content, False)
        
        if success == False:
            raise Exception("Issue creating message")
        return "Ok"

    except Exception as e:
        res = make_response("Bad request", 400)
        logging.exception(e)
        return res

app.run(debug=True, host='0.0.0.0')





