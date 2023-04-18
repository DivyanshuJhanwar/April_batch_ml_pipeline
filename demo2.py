from flask import Flask
from visa.exception import CustomException
from visa.logger import logging
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing our Custom exception file")
    except Exception as e:
        visa = CustomException(e, sys)
        logging.info(visa.error_message)
        logging.info("We are testing our logging module")
        return("Hello World")
    

if __name__=="__main__":
    app.run(debug=True)    

    
