#######################################################
# Flask Backend
# Used to initiate partner's microservice
# Returns new file contents
# Operates on XHTTPS fetch
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    return render_template('main.html')

@app.route("/microservice", methods=["GET", "POST"])
def microservice():
    # Activate microservice call
    filepath = "C:/Users/Preston/.vscode/OnTheSong/returned_song.txt"
    fileWrite = open(filepath, "w")
    fileWrite.write("run")
    fileWrite.close()

    time.sleep(4)

    # Open and return file contents
    file = open(filepath, "r")
    return file.read()

if __name__ == '__main__':
    app.run()