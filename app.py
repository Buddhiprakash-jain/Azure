from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Linux World!  <b> Hello buddhijain </b>  <img src=https://mystorage1bp.blob.core.windows.net/myimage/1614800984310.jpg />"
