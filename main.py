from flask import Flask, request
import logging
from waitress import serve

logging.basicConfig()
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def hello_world():
    ip_addr = request.environ['REMOTE_ADDR']
    logger.info(f"GET / FROM: {ip_addr}")
    return "OK!"

if __name__ == '__main__':
    

    
    serve(app, host="0.0.0.0", port=8080)