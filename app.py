from flask import Flask, jsonify, make_response, current_app

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    current_app.logger.info('Hello from path!')
    return jsonify(message='Hello from path!')


def hello_cron(event, context):
    import logging
    logging.error("hello cron")
    return True

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
