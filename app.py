from flask import Flask
from flask import json
import logging

app = Flask(__name__)
log_format = "%(asctime)s, %(funcName)s - %(message)s "
logger = logging.getLogger()
logging.basicConfig(filename="app.log", format=log_format, level=logging.DEBUG)


@app.route("/")
def hello():
    logger.info("endpoint was reached")
    return "Hello World!"


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    logger.info("endpoint was reached")
    return response


@app.route("/matrix")
def matrix():
    response = app.response_class(
        response=json.dumps({"status": "sucess", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    logger.info("endpoint was reached")
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
