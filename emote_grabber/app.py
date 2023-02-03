from flask import Flask
from emote_grabber.grabber import emote_grabber 
app = Flask(__name__)

eg = emote_grabber()

@app.route('/<channel_name>')
def get_emotes(channel_name):
    if channel_name == 'favicon.ico' :
       return ''
    return eg.get_emotes(channel_name)


if __name__ == '__main__':
   app.run('0.0.0.0', port=5001)
