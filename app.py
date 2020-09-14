import flask
from flask import request, jsonify
from youtube_downloader import YoutubeDownloader
from flask import Markup
from gunicorn.http import message

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def homepage():
    return flask.render_template('index.html')

@app.route('/get', methods=['GET'])
def encryptVizener():
    if 'url' in request.args:
        url= request.args['url']
    else:
        return "Error: You must provide url"

    print(url)
    downloader = YoutubeDownloader()
    downloader.downlaod([url])

@app.route('/decrypt/vizener', methods=['GET'])
def decryptVizener():
   if 'encrypted' in request.args: 
       encrypted = request.args['encrypted']
   else:
       return "Error: Yout must provide text for decryption"

   decrypted, key = vizener.decrypt(encrypted)
   return flask.jsonify( decrypted= decrypted, key = key) 

if __name__=="__main__":
    app.run()