#######################################################
# Flask Backend
# Used to initiate partner's microservice
# Returns new file contents
# Operates on XHTTPS fetch
#######################################################

from flask import Flask, request, jsonify, render_template, send_from_directory
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

    file = open(filepath, "r")
    return file.read()

@app.route('/songs/dieforyou.mp3')
def getDieForYou():
    return send_from_directory(app.static_folder, '/static/songs/dieforyou.mp3')

if __name__ == '__main__':
    app.run()