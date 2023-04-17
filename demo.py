from flask import Flask
from visa.logger import logging              # Create one API using Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("We are testing our logging file")
    return "Hello Worlds"

if __name__=="__main__":
    app.run(debug=True) 


