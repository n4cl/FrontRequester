from flask import Flask, jsonify

from logging import getLogger, StreamHandler, Formatter, DEBUG

logger = getLogger(__name__)
formatter = Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

app = Flask(__name__)

@app.route('/')
def hello():
    logger.debug('hello')
    return jsonify({"response": "hello world"}), 200
